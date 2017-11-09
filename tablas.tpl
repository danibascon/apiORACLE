%include('header.tpl')
<br>
	<h1>BASE DE DATOS DE CONFLICTOS BELICOS</h1>
	<h1>Tablas disponibles son:</h1>
	% for a in lista:
		<p><strong>{{a}}</strong></p>
	%end
<br>
	<h1>¿Que tabla quieres que mostremos?</h1>
	<form action="/consulta" method="post">
		<input type="text" name="tabla" required/>
		<input type="submit" value="Enviar">
	</form>
%include('footer.tpl')
