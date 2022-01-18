message = document.querySelector('#message')
console.log(`charcode: ${'a'.charCodeAt(0)}`)
message.addEventListener("input", encryptMessage)

function encryptMessage(e) {
    // console.log(e.target.value)
    let plainText = e.target.value
    let encryptedMessage = ''
    for(let a = 0; a < plainText.length; a++){
        let cur = plainText[a];
        let cur_code = cur.charCodeAt(0);
        let change_char_by = 0
        if (cur_code >= 'a'.charCodeAt(0) && cur_code <= 'z'.charCodeAt(0)){            
            change_char_by = 'z'.charCodeAt(0) + 'a'.charCodeAt(0)
        
        }else if(cur_code >= 'A'.charCodeAt(0) && cur_code <= 'Z'.charCodeAt(0)){
            change_char_by = 'A'.charCodeAt(0) + 'Z'.charCodeAt(0)
        }else{
            change_char_by = 2 * cur_code
        }
        k = String.fromCharCode(change_char_by - cur_code);
        encryptedMessage = encryptedMessage.concat(k)
    }
    // console.log(encryptedMessage)
    // document.querySelector('#encrypted-message').innerHTML = encryptedMessage
    document.querySelector('#ans').value = encryptedMessage
    // document.querySelector('#display').value = encryptedMessage

}