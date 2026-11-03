"""兼容入口；实现位于 news_classifier.evaluation.evaluate。"""
from .evaluation.evaluate import evaluate_checkpoint,main


if __name__=="__main__":
    main()
