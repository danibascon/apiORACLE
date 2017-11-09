%include('header.tpl')
<br>
	<h1>BIENVENIDOS A ORACLE</h1>
	<form action="/login" method="post">
		<label>Nombre del usuario:</label>
		<input type="text" name="user" required/>
		<label>Passwd del usuario:</label>
		<input type="password" name="passwd" required/>
		<input type="submit" value="Enviar">
	</form>
<br>
<p><a href="/">Volver atras</a></p>
%include('footer.tpl')
