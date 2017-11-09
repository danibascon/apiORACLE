%include('header.tpl')
<br>
	<h1>BASE DE DATOS DE CONFLICTOS BELICOS</h1>
	<h2>Resultado de busqueda de la tabla {{tabla}}:</h2>
	% for a in lista2:
		<p>{{a}}</p>
	%end
<br>
<br>
	<h1>Vamos a realizar un join, en el cual mostraremos el </h1>
	<h1>numero de afectados que es la suma de heridos y muertos</h1>
	<h1>Los paises disponibles son:</h1>
	% for a in lista:
		<p><strong>{{a}}</strong></p>
	%end
<br>
	<h1>¿Que tabla quieres que mostremos?</h1>
	<form action="/join" method="post">
		<input type="text" name="pais" required/>
		<input type="submit" value="Enviar">
	</form>
%include('footer.tpl')
