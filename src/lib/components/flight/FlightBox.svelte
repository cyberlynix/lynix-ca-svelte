<script>
	import FlightProgress from './FlightProgress.svelte';
</script>

<div class="box">
	<div class="test2" style="">
		<h1 style="color:#fff;">AC 647</h1>
		<p class="badge-text" style="margin-left:2rem;">Awaiting Arrival</p>
	</div>
	<div class="flight-time">
		<FlightProgress />
	</div>
	<div class="test">
		<div class="departure">
			<h2>YQM (Moncton)</h2>
			5:10 am, March 15th 2024
		</div>
		<div class="arrival">
			<h2>YYZ (Toronto)</h2>
			6:42 am, March 15th 2024
		</div>
		<hr />
		<div class="updated">Updated 0min ago</div>
		<div class="source">Source: Lynix API</div>
	</div>
</div>

<style>
    .badge-text {
        background: #272a2c;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 999px;
        font-weight: 700;
    }
    .test2 { 
        display:flex;
        flex-direction: row;
        place-items: center;
        align-items: center;
    }
	.box {
		display: flex;
		flex-direction: column;
		justify-content: center;
		border: #555 1px solid;
		border-radius: 0.5rem;
		width: 750px;
	}

	.box .test2 {
		font-weight: 700;
		padding: 0 2rem;
		margin-top: 1rem;
	}

	.box .test {
		display: grid;
		grid-template-columns: 1fr 1fr;
		grid-gap: 0.2rem;
		padding: 0.8rem 2rem;
	}

	hr {
		grid-column: span 2;
		border: none;
		border-top: #555 1px solid;
		width: 100%;
		margin: 0.6rem 0;
	}

	.flight-time {
		grid-column: span 2;
	}

	.updated,
	.source {
		color: #ffffffa0;
		font-size: 0.8rem;
		padding: 0.5rem 0;
	}

	.departure {
		border-right: #555 1px solid;
		margin-right: 1rem;
	}
</style>
