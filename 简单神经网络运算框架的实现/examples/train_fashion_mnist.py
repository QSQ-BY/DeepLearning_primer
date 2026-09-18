from mininn.data import load_idx_images,load_idx_labels
import numpy as np
from mininn import Conv2D,BatchNorm,Linear, ReLU, SGD, Sequential, SoftmaxCrossEntropyLoss,Flatten
import time
import argparse
def _load_dataset(image_path,label_path):
    images = load_idx_images(image_path)
    labels = load_idx_labels(label_path)

    if(images.shape[0] != labels.shape[0]):
        raise ValueError(
            f"sample count mismatch: "
            f"{images.shape[0]} images, {labels.shape[0]} labels"
        )

    return images,labels

def _batch_indices(sample_count,batch_size,rng = None):
    indices = np.arange(sample_count)
    if(rng is not None):
        rng.shuffle(indices)
    for start in range(0,sample_count,batch_size):
        yield indices[start:min(start + batch_size,sample_count)]

def _set_training(network,training):
    for layer in network.layers:
        if(isinstance(layer,BatchNorm)):
            if(training):
                layer.train()
            else:
                layer.eval()

def _train_one_epoch(network,images,labels,loss_function
                    ,optimizer,batch_size,rng,):
    sample_count = images.shape[0]
    if(sample_count <= 0):
        raise ValueError("training data must not be empty in training")
    if(batch_size <= 0):
        raise ValueError("batch_size must be positive in training")

    _set_training(network,True)

    total_loss = 0.0
    total_correct = 0

    for indices in _batch_indices(sample_count,batch_size,rng):
        batch_images = images[indices]
        batch_labels = labels[indices]

        logits = network.forward(batch_images)
        loss = loss_function.forward(logits,batch_labels)

        total_loss += loss*len(indices)
        predictions = np.argmax(logits,axis = 1)
        total_correct += np.sum(predictions == batch_labels)

        grad_output = loss_function.backward()
        grad_input = network.backward(grad_output)

        optimizer.step()

    return total_loss / sample_count,total_correct / sample_count

def _evaluate(network,images,labels,loss_function,batch_size):
    sample_count = images.shape[0]
    if(sample_count <= 0):
        raise ValueError("training data must not be empty in evaluating")
    if(batch_size <= 0):
        raise ValueError("batch_size must be positive in evaluating")
    _set_training(network,False)
    rng = np.random.default_rng(7)

    batch_indices = list(_batch_indices(sample_count,batch_size,rng))
    total_loss = 0.0
    total_correct = 0
    for indices in batch_indices:
        batch_images = images[indices]
        batch_labels = labels[indices]

        logits = network.forward(batch_images)
        loss = loss_function.forward(logits,batch_labels)

        total_loss += loss*len(indices)
        predictions = np.argmax(logits,axis = 1)
        total_correct += np.sum(predictions == batch_labels)

    _set_training(network,True)
    return total_loss / sample_count,total_correct / sample_count

def _build_network(rng = None):
    if(rng is None):
        rng = np.random.default_rng()
    network = Sequential(
        Conv2D(in_channels = 1,out_channels = 4,
            kernel_size = 3,stride = 2,padding = 1,rng = rng),
        BatchNorm(num_features = 4),
        ReLU(),
        Conv2D(in_channels = 4,out_channels = 8,
            kernel_size = 3,stride = 2,padding = 1,rng = rng),
        BatchNorm(num_features = 8),
        ReLU(),
        Flatten(),

        Linear(8*7*7,20,rng = rng),
        BatchNorm(num_features = 20),
        ReLU(),
        Linear(20,10,rng = rng)
    )

    return network

def _fit(network,train_images,train_labels,test_images,test_labels,epochs,batch_size,learning_rate,rng = None):
    if(rng is None):
        rng = np.random.default_rng()
    loss_function = SoftmaxCrossEntropyLoss()
    optimizer = SGD(network.parameters(),network.gradients(),learning_rate)
    history = []
    for epoch in range(1,epochs+1):
        start_time = time.perf_counter()
        train_loss,train_accuracy = _train_one_epoch(network,train_images,train_labels,loss_function,optimizer,batch_size,rng,)
        test_loss,test_accuracy = _evaluate(network,test_images,test_labels,loss_function,batch_size,)
        elapsed_seconds = time.perf_counter() - start_time
        history.append({
            "epoch": epoch,
            "train_loss": train_loss,
            "train_accuracy": train_accuracy,
            "test_loss": test_loss,
            "test_accuracy": test_accuracy,
            "elapsed_seconds":elapsed_seconds,
        })
        print(
            f"epoch={epoch}/{epochs} "
            f"train_loss={train_loss:.6f} "
            f"train_accuracy={train_accuracy:.2%} "
            f"test_loss={test_loss:.6f} "
            f"test_accuracy={test_accuracy:.2%} "
            f"time = {elapsed_seconds:.2f}s"
        )

    return history

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("train_images")
    parser.add_argument("train_labels")
    parser.add_argument("test_images")
    parser.add_argument("test_labels")
    args = parser.parse_args()

    train_images,train_labels = _load_dataset(
        args.train_images,
        args.train_labels
    )
    test_images, test_labels = _load_dataset(
        args.test_images,
        args.test_labels,
    )
    if train_images.shape[0] < 2000:
        raise ValueError("training dataset must contain at least 2000 samples")
    if test_images.shape[0] < 1000:
        raise ValueError("test dataset must contain at least 1000 samples")

    train_images = train_images[:2000]
    train_labels = train_labels[:2000]
    test_images = test_images[:1000]
    test_labels = test_labels[:1000]

    rng = np.random.default_rng(42)
    network = _build_network(rng)

    history = _fit(
        network,
        train_images,
        train_labels,
        test_images,
        test_labels,
        epochs=10,
        batch_size=32,
        learning_rate=0.05,
        rng=rng,
    )


if __name__ == "__main__":
    main()