<script lang="ts">
	let isOpen = false;
	const toggleNav = () => {
		isOpen = !isOpen;
	};
</script>

<header>
	<h1 class="text-effect">LYNIX</h1>
	<nav class={isOpen ? 'open' : ''}>
		<a href="/">Projects</a>
		<a href="/blog">Blog</a>
		<a href="/references">References</a>
		<a href="/about">About</a>
		<a href="/contact">Contact</a>
		<a href="/login" class="login">Login</a>
	</nav>
	<button class="nav-button" on:click={toggleNav} aria-label="Toggle Navigation">
        <svg height="24px" width="24px" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 17 14">
            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M1 1h15M1 7h15M1 13h15"/>
        </svg>
	</button>
</header>

<style>
	.text-effect {
		text-shadow: 5px 5px #0c4a6e;
		color: #0ea5e9;
		font-size: 2.5rem;
	}

	header {
		background: #121212;
		color: #fff;
		padding: 1rem;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		gap: 1rem;
		padding: 1.5em 0;
		border-bottom: 1px solid #ffffff20;
        width: 100%;
	}

	nav {
		display: flex;
		flex-direction: row;
		align-items: center;
		justify-content: center;
		gap: 1.5rem;
	}

	nav a {
		color: #a1a1aa;
		font-size: 1.3rem;
		font-weight: 500;
		transition: color 0.3s ease;
	}

	nav a:hover {
		color: #0ea5e9;
	}

	.login {
		background: #0ea5e9;
		color: #111111;
		padding: 0.5rem 1rem;
		font-weight: 700;
		transition: background 0.3s ease;
	}

	.login:hover {
		background: #0284c7;
	}

	.nav-button {
		all: unset;
		display: none;
		text-align: center;
		justify-content: center;
		align-items: center;
        color: #a1a1aa;
	}

	@media (max-width: 520px) {
		header {
			justify-content: space-between;
			flex-direction: row;
			padding: 1em 2em;
		}

		nav {
			opacity: 0;
			display: flex;
			position: fixed;
			top: 0;
			left: 0;
			bottom: 0;
			right: 0;
			flex-direction: column;
			background: #111111;
			transition: opacity 0.3s;
			pointer-events: none;
            z-index: 1000;
		}

		nav a {
			transition: transform 0.3s;
			transform: translateY(-30px);
		}

		nav.open a {
			transform: translateY(0px);
		}

		nav.open {
			opacity: 1;
			pointer-events: all;
		}

		.nav-button {
			display: flex;
			z-index: 10000;
			transition: transform 0.3s;
		}

		nav.open + .nav-button {
			transform: rotate(90deg);
		}
	}
</style>
