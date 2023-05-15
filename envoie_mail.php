<?php
if(isset($_POST['email'])) {
    $to = $_POST['destinataire'];  
    $subject = "Nouveau message depuis le formulaire de contact";
    $message = "Nom: " . $_POST['nom'] . "\n\n";
    $message .= "Email: " . $_POST['email'] . "\n\n";
    $message .= "Message: " . $_POST['message'] . "\n\n";
    $headers = "From: " . $_POST['email'];

    if(mail($to, $subject, $message, $headers)) {
        echo "Votre e-mail a été envoyé avec succès.";
    } else {
        echo "Une erreur s'est produite lors de l'envoi de l'e-mail.";
    }
}
?>
