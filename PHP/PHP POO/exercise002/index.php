<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <pre>
    <?php
        require_once 'Caneta.php';

        $caneta1 = new Caneta("BIC","Azul", 0.5);

        print_r($caneta1);

        /*Usando __contruct || Caneta() como métodos contrutores:

        $caneta1->setModelo("BIC");
        $caneta1->setPonta(0.5);

        echo "Eu tenho uma caneta {$caneta1->getModelo()} de ponta {$caneta1->getPonta()}"
        */

    ?>
    </pre>
</body>
</html>