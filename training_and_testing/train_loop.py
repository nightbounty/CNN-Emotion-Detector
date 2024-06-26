from utils.tools_lib import *
from training_and_testing.train import train
from training_and_testing.test import test

def train_loop(model, optimizer, train_loader, val_loader, loss, epochs, patience):
    train_losses, train_accuracies = [], []
    val_losses, val_accuracies     = [], []

    best_val_loss = float('inf')
    counter       = 0

    for epoch in tqdm(range(epochs), desc='epochs'):
        train_loss, train_accuracy = train(train_loader, model, loss, optimizer)
        val_loss, val_accuracy     = test(val_loader, model, loss)

        train_losses.append(train_loss)
        train_accuracies.append(train_accuracy)
        val_losses.append(val_loss)
        val_accuracies.append(val_accuracy)

        if val_loss < best_val_loss:
            best_val_loss = val_loss
            counter       = 0
        else:
            if counter >= patience:
                print(f"Early stopping at epoch {epoch}")
                break
            counter += 1

    return train_losses, train_accuracies, val_losses, val_accuracies