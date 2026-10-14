(() => {
  'use strict';

  // Node canvases: hovering or focusing a node lights it, its neighbours
  // and the edges between them; everything else recedes.
  document.querySelectorAll('[data-canvas]').forEach((canvas) => {
    const edges = [...canvas.querySelectorAll('.edge[data-from]')];
    const nodes = new Map([...canvas.querySelectorAll('.node[data-id]')].map((n) => [n.dataset.id, n]));

    const light = (id) => {
      canvas.classList.add('is-focusing');
      nodes.get(id).classList.add('is-lit');
      edges.forEach((edge) => {
        const { from, to } = edge.dataset;
        if (from !== id && to !== id) return;
        edge.classList.add('is-lit');
        nodes.get(from === id ? to : from)?.classList.add('is-lit');
      });
    };

    const clear = () => {
      canvas.classList.remove('is-focusing');
      canvas.querySelectorAll('.is-lit').forEach((el) => el.classList.remove('is-lit'));
    };

    nodes.forEach((node, id) => {
      node.addEventListener('pointerenter', () => light(id));
      node.addEventListener('pointerleave', clear);
      node.addEventListener('focus', () => light(id));
      node.addEventListener('blur', clear);
    });
  });
})();
