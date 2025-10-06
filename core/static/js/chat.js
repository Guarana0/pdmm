(function(){
  const setPulseAnimVar = () => {
    const isDark = document.documentElement.classList.contains('dark');
    const panel = document.getElementById('chat-panel');
    if (!panel) return;
    panel.style.setProperty('--chatPulseAnim', isDark ? 'chatPulseDark' : 'chatPulseLight');
  };

  const ensureElements = () => {
    return {
      toggle: document.getElementById('chat-toggle'),
      close: document.getElementById('chat-close'),
      panel: document.getElementById('chat-panel'),
      input: document.getElementById('chat-input'),
      send: document.getElementById('chat-send'),
      messages: document.getElementById('chat-messages')
    };
  };

  const appendMessage = (text, who='user') => {
    const msgs = document.getElementById('chat-messages');
    if (!msgs) return;
    const div = document.createElement('div');
    div.className = `msg ${who}`;
    div.textContent = text;
    msgs.appendChild(div);
    msgs.scrollTop = msgs.scrollHeight;
  };

  const sendMessage = () => {
    const input = document.getElementById('chat-input');
    if (!input) return;
    const text = input.value.trim();
    if (!text) return;
    appendMessage(text, 'user');
    input.value = '';
    setTimeout(() => appendMessage('Recebido: ' + text, 'bot'), 400);
  };

  const openPanel = () => {
    const { panel, input } = ensureElements();
    if (!panel) return;
    setPulseAnimVar();
    panel.classList.add('open');
    panel.setAttribute('aria-modal', 'true');
    panel.style.display = 'flex';
    setTimeout(() => input && input.focus(), 150);
  };

  const closePanel = () => {
    const { panel } = ensureElements();
    if (!panel) return;
    panel.classList.remove('open');
    panel.setAttribute('aria-modal', 'false');
    panel.style.display = 'none';
  };

  const togglePanel = () => {
    const { panel } = ensureElements();
    if (!panel) return;
    if (panel.classList.contains('open')) closePanel(); else openPanel();
  };

  document.addEventListener('DOMContentLoaded', () => {
    const { toggle, close, send, input } = ensureElements();
    if (toggle) toggle.addEventListener('click', togglePanel);
    if (close) close.addEventListener('click', closePanel);
    if (send) send.addEventListener('click', sendMessage);
    if (input) input.addEventListener('keydown', (e) => { if (e.key === 'Enter') sendMessage(); });

    const themeToggle = document.getElementById('theme-toggle');
    if (themeToggle) {
      themeToggle.addEventListener('click', () => setTimeout(setPulseAnimVar, 0));
    }

    setPulseAnimVar();
  });
})();
