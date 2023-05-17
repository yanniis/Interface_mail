function ajouterAdresse(event) {
    event.preventDefault(); // Permet de retarder l'envoi du formulaire
  
    // Récupérer la valeur du champ de saisie d'adresse e-mail
    const newMail = document.getElementById('destinataire').value;
  

    const adressList = document.getElementById('defaultEmails');
    let options = adressList.getElementsByTagName('option');
    for (let i = 0; i < options.length; i++) {
      if (options[i].value === newMail) {
        return; 
      }
    }
  
    // Ajout de la nouvelle adresse 
    const newOption = document.createElement('option');
    newOption.value = newMail;
    adressList.appendChild(newOption);
  
    event.target.reset();
    event.target.submit();
  }
  