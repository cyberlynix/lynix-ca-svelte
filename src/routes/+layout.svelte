<script>
    import Navbar from '$lib/components/Navbar.svelte';
</script>

<div class="main">
	<Navbar/>
	<div class="alert">
		Due to some breaking backend API changes that are pending implementation, some links may not be functional yet.<br/>
		This afffects the Frontend only, and the API is still functional.
	</div>
	<slot />
</div>

<style>
	:global(*) {
		box-sizing: border-box;
		margin: 0;
		padding: 0;
		/* just so we can preview a non-serif font */
	}

	.alert {
		padding: 1rem;
		background: #f44336;
		color: #fff;
		text-align: center;
		font-size: 20px;
		font-weight: 500;
	}

	.main {
		display: flex;
		flex-direction: column;
		height: 100vh;
		width: 100%;
	}
</style>
