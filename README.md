# ME17 - Cat vs Fox Classifier

## Live App
https://me17-group-cat-fox-classifier-dolncujh2b4hej4dg87sw3.streamlit.app/

## Group Members
1. Chinwendu Solomon Chimezuru (Admin) - 22/EG/ME/1728 - GitHub: chinwendusolomon066-art
2. Bassey Ephraim Linus - 22/EG/ME/1778 - GitHub: basseyephraim0-cell
3. Ekping, Alkali Barry - 22/EG/ME/1808 - GitHub: barryalkali2004-dot
4. Essien, Imoh Boniface - 22/EG/ME/1748 - GitHub: Imoh-art
5. Bassey, Abasi-ifreke Dominus - 22/EG/ME/1788 - GitHub: leoabass
6. James Abasiodu Paul - 22/EG/ME/1708 - GitHub: abasiodujames637-code
7. George Precious - 22/EG/ME/1718 - preciousgeorge2004-creator
8. Jackson Victor Friday - 22/EG/ME/1758 - GitHub: victorjack1243-glitch
9. Silas, Solomon God'spower - 22/EG/ME/1698 - GitHub: solocheriisilas-sudo

## Report

This project implements a binary image classifier distinguishing cats from foxes, developed for the ME17 group assignment. The dataset was sourced from Kaggle ("Animal Image Dataset - Cats, Dogs, and Foxes" by snmahsa), using only the cat and fox classes (165 training, 39 validation images). A MobileNetV2 transfer learning model was trained in Google Colab using TensorFlow/Keras, achieving 92-97% validation accuracy across training runs. The model was deployed as a Streamlit web application, allowing users to upload an image and receive a predicted label with confidence score. Key challenges included a Keras layer serialization error when loading `.h5` models, resolved by saving in the newer `.keras` format, and a Python version mismatch on both local and cloud environments, resolved by specifying Python 3.11 (TensorFlow's supported version) instead of the default 3.14. Future improvements could include expanding the dataset and adding richer UI feedback.

## How to Use
1. Visit the live app link above
2. Click "Upload an image..."
3. Select a cat or fox image (JPG/PNG)
4. View the predicted label and confidence score
