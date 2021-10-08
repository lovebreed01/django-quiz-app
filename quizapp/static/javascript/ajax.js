var xhr = new XMLHttpRequest();
    xhr.open('GET', '{% url "ajax-detail" category.pk %}')
    xhr.onload= function(){
      if (this.status == 200){
        data = JSON.parse(this.responseText)
        console.log(data)
        console.log(typeof(data));
        data.forEach(el => {
           var body = `
           
              <h1>${el.question_text}</h1>
              <ul>
              <li>${el.answers[0].data}</li>
              <li>${el.answers[1].data}</li>
              <li>${el.answers[2].data}</li>
              <b>${el.correct}</b>
              
              </ul>
            `
            document.getElementById('questions').innerHTML = body;
          
        });
         
      }
    }
    xhr.onerror = function(){
      document.body.innerHTML= `
      <div> Error${this.status, this.statusText}</div>
            `
    }
    xhr.send();

    