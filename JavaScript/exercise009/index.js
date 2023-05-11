//Condições Aninhadas
function enviar(){

    var idade = document.querySelector('#txtIdade').value;
    let result = document.querySelector('#result');

    if (idade < 16){
        result.textContent = `Você não está apto a votar pois possui ${idade} anos`;
    }
    else if(idade < 18 || idade > 65){
        result.textContent = `Você possui voto facultativo pois possui ${idade} anos`;
    }
    else{
        result.textContent = `Você está apto a votar pois possui ${idade} anos`;
    }
}

//Condições Multiplas

function exibirData(){

let agora = new Date();
let dia_semana = agora.getDay();
let mes = agora.getMonth();
let ano = agora.getUTCFullYear();
let hora = agora.getHours();

switch(dia_semana){
    case 0:
        document.write(`Domingo, ${dia_semana}/${mes}/${ano} - ${hora}Horas (Horário de Brasília)`);
        break
    case 1:
        document.write(`Segunda, ${dia_semana}/${mes}/${ano} - ${hora}Horas (Horário de Brasília)`);
        break
    case 2:
        document.write(`Terça, ${dia_semana}/${mes}/${ano} - ${hora}Horas (Horário de Brasília)`);
        break
    case 3:
        document.write(`Quarta, ${dia_semana}/${mes}/${ano} - ${hora}Horas (Horário de Brasília)`);
        break
    case 4:
        document.write(`Quinta, ${dia_semana}/${mes}/${ano} - ${hora}Horas (Horário de Brasília)`);
        break
    case 5:
        document.write(`Sexta, ${dia_semana}/${mes}/${ano} - ${hora}Horas (Horário de Brasília)`);
        break
    case 6:
        document.write(`Sábado, ${dia_semana}/${mes}/${ano} - ${hora}Horas  (Horário de Brasília)`);
        break    
    default:
        window.print(`O dia não existe, ${dia_semana}/${mes}/${ano} - ${hora}Horas(Horário de Brasília)`);
        break
}
}