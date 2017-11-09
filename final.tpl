%include('header.tpl')
<br>
	<h1>BASE DE DATOS DE CONFLICTOS BELICOS</h1>
	<h2>Resultado de busqueda del pais {{pais}}:</h2>
	% for a in lista2:
		<p><strong>{{a[0]}}: numero de afectados -> {{a[1]}}</strong></p>
	%end
<br>
<br>
	<h1>¿Que quieres hacer ahora?</h1>
	<p><a href="/">Volver a login</a></p>

%include('footer.tpl')
