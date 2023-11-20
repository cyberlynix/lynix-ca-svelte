<div class="progress">
	<div class="fill">
		<span class="icon">
			<!-- replace with actual icon component -->
			<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
				><path
					d="M20.56 3.91C21.15 4.5 21.15 5.45 20.56 6.03L16.67 9.92L18.79 19.11L17.38 20.53L13.5 13.1L9.6 17L9.96 19.47L8.89 20.53L7.13 17.35L3.94 15.58L5 14.5L7.5 14.87L11.37 11L3.94 7.09L5.36 5.68L14.55 7.8L18.44 3.91C19 3.33 20 3.33 20.56 3.91Z"
				/></svg
			>
		</span>
	</div>
</div>

<style>
	.progress {
		background: #333;
		border-radius: 1000rem;
		height: 0.4rem;
		margin: 1rem 2rem;
	}

	.fill {
		background: #777;
		border-radius: 1000rem;
		height: 100%;
		width: 1%;
		position: relative;
		display: flex;
		align-items: center;
		justify-content: center;
		/*animation: move 50s infinite ease-in-out;*/
	}

	@keyframes move {
		0% {
			width: 0%;
		}
		50% {
			width: 100%;
		}
		100% {
			width: 0%;
		}
	}

	.icon {
		position: absolute;
		width: 2rem;
		height: 2rem;
		display: flex;
		align-items: center;
		justify-content: center;
		right: -1rem;
		fill: #fff;
        transform: rotate(45deg);
	}
</style>
