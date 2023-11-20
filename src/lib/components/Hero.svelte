<script lang="ts">
</script>

<div class="hero-container">
	<div class="container">
		<div class="test">
			<div class="lynix-container">
				<img src="/lynix_solo.png" alt="Lynix" class="lynix-solo float-animation" />
				<img
					src="/lynix_signature_glitch.png"
					alt="Lynix Glitch Background"
					class="lynix-solo-bg float-animation-inverse"
				/>
			</div>
			<!-- (Image Artwork by: ProtoReese) -->
			<h1 class="title">Lynix, the IT Specialist</h1>
			<p>
				VR enthusiast, Developer, Cybersecurity Student, and Furry, I'm seeking opportunities to
				change the world for better for everyone with IT.
			</p>

            <div class="btns-container">
                <a href="/projects" class="btn-projects">Projects</a>
                <a href="/contact" class="btn-contact">Contact Me</a>
            </div>
		</div>
	</div>
</div>

<style>
    .btns-container {
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        gap: 1rem;
        margin-top: 15px;
    }

    .btn-contact, .btn-projects {
        color: black;
        padding: 0.5rem 1rem;
        font-size: 25px;
        font-weight: 600;
    }

    .btn-contact {
        background: rgb(34 197 94);
    }

    .btn-projects {
        background: rgb(6 182 212);

    }
    

    .test {
        max-width: 56rem;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

	.title {
		font-size: 3rem;
		font-weight: 700;
		color: #0ea5e9;
		text-align: center;
		text-shadow: 5px 5px #0c4a6e;
	}

	.hero-container {
		background: url(/test-v3.jpg);
		background-size: cover;
		background-position: center;
		background-repeat: no-repeat;
		height: 100vh;
	}

	.container {
		height: 100%;
		background-color: rgba(0, 0, 0, 0.7);
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		font-size: 50px;
	}

	.container p {
		margin-top: 5px;
		font-size: 1.5rem;
		font-weight: 500;
		color: #a1a1aa;
		text-align: center;
	}

	.lynix-container {
		position: relative;
		width: 100%;
		max-width: 450px;
		height: 355px;
	}

	.lynix-solo,
	.lynix-solo-bg {
		position: absolute;
		top: 0;
		left: 0;
		width: 100%;
		height: auto;
	}

	.lynix-solo {
		z-index: 2;
	}

	.lynix-solo-bg {
		z-index: 1;
	}

	@keyframes float {
		0%,
		100% {
			transform: translateY(-5px);
		}

		50% {
			transform: translateY(-15px);
		}
	}

	@keyframes float-inverse {
		0%,
		100% {
			transform: translateY(-15px);
		}

		50% {
			transform: translateY(-5px);
		}
	}

	.float-animation {
		animation: float 3s ease-in-out infinite;
	}

	.float-animation-inverse {
		animation: float-inverse 3s ease-in-out infinite;
	}
</style>
