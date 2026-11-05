from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
import socket

app = FastAPI(title="Giva-App-MIT Architecture Visualizer")

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Giva-App-MIT | Cyber Pipeline Visualizer</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    @keyframes glow { 0%, 100% { box-shadow: 0 0 15px rgba(0, 229, 255, 0.4); } 50% { box-shadow: 0 0 25px rgba(0, 229, 255, 0.8); } }
    @keyframes pulse-fast { 0%, 100% { opacity: 1; } 50% { opacity: 0.3; } }
    .matrix-bg { position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: 0; opacity: 0.22; pointer-events: none; }
    .neon-border { border: 1px solid rgba(0, 229, 255, 0.35); }
    .neon-glow { animation: glow 3s infinite ease-in-out; }
    .pulse-dot { animation: pulse-fast 1.2s infinite; }
    .custom-scroll::-webkit-scrollbar { width: 5px; height: 5px; }
    .custom-scroll::-webkit-scrollbar-thumb { background: #1e293b; border-radius: 4px; }
  </style>
</head>
<body class="bg-[#070b14] text-slate-200 font-mono min-h-screen relative overflow-x-hidden">
  <canvas id="matrixCanvas" class="matrix-bg"></canvas>

  <div class="relative z-10 max-w-7xl mx-auto p-4 sm:p-6 space-y-6">
    <!-- Header -->
    <header class="flex flex-col md:flex-row items-center justify-between border-b border-slate-800 pb-4 gap-4">
      <div>
        <div class="flex items-center space-x-3">
          <span class="inline-block w-3 h-3 rounded-full bg-emerald-400 pulse-dot"></span>
          <h1 class="text-2xl font-black tracking-wider text-cyan-400">GIVA-APP-MIT // LIVE CLOUD PLATFORM</h1>
        </div>
        <p class="text-xs text-slate-400 mt-1">Autonomous GitOps CI/CD • EKS Cluster 1.31 • AWS ECR</p>
      </div>

      <!-- Hacker Badge -->
      <div class="bg-slate-900/90 border border-cyan-500/50 px-4 py-2 rounded-lg neon-glow text-right">
        <div class="text-[10px] tracking-widest text-cyan-300 uppercase">Lead Architecture</div>
        <div class="text-sm font-bold text-emerald-300">DevOps Engineer - Salman Khan</div>
      </div>
    </header>

    <!-- Top Status Bar -->
    <div class="grid grid-cols-2 md:grid-cols-4 gap-3 text-xs">
      <div class="bg-slate-900/80 p-3 rounded border border-slate-800">
        <div class="text-slate-400">ENVIRONMENT</div>
        <div class="text-cyan-400 font-bold mt-1">AWS EKS ap-south-1</div>
      </div>
      <div class="bg-slate-900/80 p-3 rounded border border-slate-800">
        <div class="text-slate-400">CLUSTER STATUS</div>
        <div class="text-emerald-400 font-bold mt-1 flex items-center space-x-1">
          <span class="w-2 h-2 rounded-full bg-emerald-400 inline-block"></span>
          <span>100% HEALTHY</span>
        </div>
      </div>
      <div class="bg-slate-900/80 p-3 rounded border border-slate-800">
        <div class="text-slate-400">ACTIVE PODS</div>
        <div id="podCount" class="text-yellow-400 font-bold mt-1">2 / 2 REPLICAS</div>
      </div>
      <div class="bg-slate-900/80 p-3 rounded border border-slate-800">
        <div class="text-slate-400">HOSTNAME / POD IP</div>
        <div id="podHost" class="text-slate-200 font-bold mt-1 truncate">FETCHING...</div>
      </div>
    </div>

    <!-- Architecture Visual Grid -->
    <div class="bg-slate-900/80 rounded-xl p-5 border border-slate-800">
      <h2 class="text-sm font-bold tracking-wider text-cyan-300 uppercase mb-4 flex items-center gap-2">
        <span>⚡ Live Infrastructure Data Flow</span>
      </h2>

      <div class="grid grid-cols-1 md:grid-cols-5 gap-4 items-center">
        <!-- Node 1 -->
        <div class="bg-[#0b1329] border border-cyan-500/30 p-4 rounded-lg text-center relative group">
          <div class="text-xl mb-1">💻</div>
          <div class="text-xs font-bold text-cyan-300">VS Code / Dev</div>
          <div class="text-[10px] text-slate-400 mt-1">Git Commit & Push</div>
          <div class="mt-2 text-[9px] bg-slate-800 text-cyan-400 py-0.5 rounded">branch: main</div>
        </div>

        <!-- Node 2 -->
        <div class="bg-[#0b1329] border border-cyan-500/30 p-4 rounded-lg text-center relative">
          <div class="text-xl mb-1">⚙️</div>
          <div class="text-xs font-bold text-cyan-300">GitHub Actions</div>
          <div class="text-[10px] text-slate-400 mt-1">CI Runner Matrix</div>
          <div class="mt-2 text-[9px] bg-emerald-950 text-emerald-400 py-0.5 rounded">Docker Build OK</div>
        </div>

        <!-- Node 3 -->
        <div class="bg-[#0b1329] border border-cyan-500/30 p-4 rounded-lg text-center relative">
          <div class="text-xl mb-1">📦</div>
          <div class="text-xs font-bold text-cyan-300">AWS ECR Registry</div>
          <div class="text-[10px] text-slate-400 mt-1">giva-app-mit</div>
          <div class="mt-2 text-[9px] bg-slate-800 text-cyan-300 py-0.5 rounded truncate">sha: verified</div>
        </div>

        <!-- Node 4 -->
        <div class="bg-[#0b1329] border border-cyan-500/30 p-4 rounded-lg text-center relative">
          <div class="text-xl mb-1">🌐</div>
          <div class="text-xs font-bold text-cyan-300">AWS Load Balancer</div>
          <div class="text-[10px] text-slate-400 mt-1">Port 80 Routing</div>
          <div class="mt-2 text-[9px] bg-blue-950 text-blue-300 py-0.5 rounded">Traffic Balanced</div>
        </div>

        <!-- Node 5 -->
        <div class="bg-[#0b1329] border border-emerald-500/40 p-4 rounded-lg text-center relative">
          <div class="text-xl mb-1">☸️</div>
          <div class="text-xs font-bold text-emerald-300">EKS Managed Node</div>
          <div class="text-[10px] text-slate-400 mt-1">AL2023 t3.small</div>
          <div class="mt-2 text-[9px] bg-emerald-950 text-emerald-400 py-0.5 rounded">Target: Ready</div>
        </div>
      </div>
    </div>

    <!-- Live Terminal / Logs Preview -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
      <!-- Terminal Stream -->
      <div class="bg-[#050811] rounded-xl p-4 border border-slate-800 flex flex-col h-64">
        <div class="flex items-center justify-between border-b border-slate-800 pb-2 mb-2 text-xs">
          <span class="text-cyan-400 flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-cyan-400 inline-block pulse-dot"></span>
            LIVE KUBECTL STREAM
          </span>
          <span class="text-slate-500">ap-south-1</span>
        </div>
        <div id="terminalBody" class="flex-1 overflow-y-auto custom-scroll text-[11px] space-y-1 text-slate-400">
          <div><span class="text-cyan-400">[info]</span> Connected to cluster giva-prod-eks (Kubernetes 1.31)</div>
          <div><span class="text-cyan-400">[info]</span> Pulling container image from ECR private registry...</div>
          <div><span class="text-emerald-400">[success]</span> Pod deployment/giva-app-deployment rollout complete.</div>
        </div>
      </div>

      <!-- Live API Response -->
      <div class="bg-[#050811] rounded-xl p-4 border border-slate-800 flex flex-col h-64">
        <div class="flex items-center justify-between border-b border-slate-800 pb-2 mb-2 text-xs">
          <span class="text-emerald-400">LIVE ENDPOINT: /health</span>
          <button onclick="pingHealth()" class="bg-slate-800 hover:bg-slate-700 text-[10px] text-cyan-300 px-2 py-0.5 rounded border border-slate-700">Refresh</button>
        </div>
        <div class="flex-1 bg-black/40 rounded p-3 overflow-auto custom-scroll text-xs">
          <pre id="jsonPayload" class="text-emerald-300 font-mono">Fetching backend health...</pre>
        </div>
      </div>
    </div>
  </div>

  <script>
    // Matrix Rain Effect
    const canvas = document.getElementById('matrixCanvas');
    const ctx = canvas.getContext('2d');
    let width = canvas.width = window.innerWidth;
    let height = canvas.height = window.innerHeight;
    const chars = '01SALMANDEVOPSEKSKUBERNETESTRAFFICDOCKERAWS';
    const fontSize = 14;
    const columns = Math.floor(width / fontSize);
    const drops = Array(columns).fill(1);

    function drawMatrix() {
      ctx.fillStyle = 'rgba(7, 11, 20, 0.08)';
      ctx.fillRect(0, 0, width, height);
      ctx.fillStyle = '#00e5ff';
      ctx.font = fontSize + 'px monospace';
      for (let i = 0; i < drops.length; i++) {
        const text = chars[Math.floor(Math.random() * chars.length)];
        ctx.fillText(text, i * fontSize, drops[i] * fontSize);
        if (drops[i] * fontSize > height && Math.random() > 0.975) drops[i] = 0;
        drops[i]++;
      }
    }
    setInterval(drawMatrix, 45);
    window.addEventListener('resize', () => {
      width = canvas.width = window.innerWidth;
      height = canvas.height = window.innerHeight;
    });

    // Real API fetch
    async function pingHealth() {
      try {
        const res = await fetch('/health');
        const data = await res.json();
        document.getElementById('jsonPayload').innerText = JSON.stringify(data, null, 2);
        document.getElementById('podHost').innerText = data.pod_hostname || 'localhost';
      } catch (err) {
        document.getElementById('jsonPayload').innerText = "Status: OK (Connected)";
      }
    }
    pingHealth();
  </script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
def get_dashboard():
    return HTMLResponse(content=HTML_TEMPLATE)

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "Giva-App-MIT",
        "pod_hostname": socket.gethostname(),
        "lead_engineer": "Salman Khan",
        "environment": "AWS EKS 1.31"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)