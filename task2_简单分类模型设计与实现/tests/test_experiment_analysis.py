"""离线检查错误集合、指标、清洗边界与词向量导入。"""
import tempfile
import unittest
from pathlib import Path
import numpy as np
import torch
from news_classifier.evaluation.analysis import error_groups,classification_metrics
from news_classifier.data.preprocessing import clean_text
from news_classifier.data.embeddings import load_pretrained_vectors
from news_classifier.evaluation.predict import predict
from news_classifier.config import load_config
from news_classifier.models import TextCNN


class ExperimentAnalysisTests(unittest.TestCase):
    def test_prediction_restores_cleaning_rule_from_checkpoint(self):
        torch.manual_seed(7)
        config=load_config()
        config['model'].update(embed_dim=4,num_filters=3,kernel_sizes=[2,3])
        config['experiment']={'clean_text':True,'cleaning_version':'known_html_tags_v2'}
        vocab={'<PAD>':0,'<UNK>':1,'world':2,'s':3,'news':4,'cien':5,'o':6}
        model=TextCNN(len(vocab),config['model'])
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'clean.pt'
            torch.save(dict(config=config,vocab=vocab,label_names=['World','Sports','Business','Sci/Tech'],
                            model_state_dict=model.state_dict()),path)
            _,raw=predict(path,'World #39;s &lt;b&gt;news&lt;/b&gt; &lt;CIEN.O&gt;')
            _,normalized=predict(path,"World 's news CIEN.O")
        self.assertTrue(np.allclose(raw,normalized,atol=1e-7))

    def test_error_groups_are_exhaustive_and_check_alignment(self):
        groups=error_groups([0,1,2,3,0],[0,0,0,3,1],[0,1,0,1,0])
        self.assertEqual(groups,{'both_correct':[0],'fixed':[1,4],'both_wrong':[2],'new_errors':[3]})
        with self.assertRaises(ValueError): error_groups([0,1],[0],[0,1])

    def test_metrics_keep_empty_predicted_class_and_reconcile_confusion(self):
        metrics=classification_metrics([0,1,2,3],[0,1,2,2])
        self.assertEqual(metrics['correct'],3)
        self.assertEqual(metrics['accuracy'],.75)
        self.assertEqual(metrics['confusion_matrix'],[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,1,0]])
        self.assertEqual(metrics['per_class'][3]['recall'],0)
        self.assertAlmostEqual(metrics['macro_f1'],2/3)

    def test_cleaning_preserves_words_and_numbers_but_repairs_known_entities(self):
        value='Google #39;s &lt;b&gt;new&lt;/b&gt; tool costs #36;75 &amp; 10; quot;PCquot;'
        cleaned=clean_text(value)
        self.assertIn("Google 's",cleaned)
        self.assertIn('new',cleaned)
        self.assertIn('$75',cleaned)
        self.assertIn('10;',cleaned)
        self.assertNotIn('<b>',cleaned)
        self.assertNotIn('39',cleaned)
        self.assertEqual(clean_text('World Bank 2004 21-18'),'World Bank 2004 21-18')
        self.assertIn('CIEN.O',clean_text('Ciena &lt;CIEN.O&gt; stock &lt;b&gt;news&lt;/b&gt;'))

    def test_pretrained_vectors_align_by_word_and_leave_unknown_initialization(self):
        vocab={'<PAD>':0,'<UNK>':1,'bank':2,'news':3}
        initial=torch.tensor([[0.,0.],[1.,2.],[3.,4.],[5.,6.]])
        with tempfile.TemporaryDirectory() as tmp:
            source=Path(tmp)/'vectors.txt'
            source.write_text('bank 0.1 0.2\nother 0.3 0.4\n',encoding='utf-8')
            weights,metadata=load_pretrained_vectors(source,vocab,initial)
        self.assertTrue(torch.allclose(weights[2],torch.tensor([.1,.2])))
        self.assertTrue(torch.equal(weights[3],initial[3]))
        self.assertTrue(torch.equal(weights[0],torch.zeros(2)))
        self.assertEqual(metadata['matched_words'],1)


if __name__=='__main__': unittest.main()
