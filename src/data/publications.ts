export interface Publication {
  slug: string;
  year: number;
  title: string;
  venue: string;
  distinction?: string;
  authors: string;
  description: string;
  topics: string[];
  paperUrl: string;
  videoUrl: string;
  websiteUrl?: string;
  media: { src: string; type: 'image' | 'video' } | null;
}

export const publications: Publication[] = [
  {
    slug: 'pixels-to-proofs',
    year: 2026,
    paperUrl: 'https://arxiv.org/pdf/2606.15594',
    videoUrl: 'https://www.youtube.com/watch?v=3sYYNSQqwSQ',
    websiteUrl: 'https://trustworthyrobotics.github.io/SLS-squared/',
    media: { src: '/projects/pixels-to-proofs/assets/thumbnail.mp4', type: 'video' },
    title: 'Pixels to Proofs: Probabilistically Safe Latent World Model Control via Parallel Conformal Robust MPC',
    venue: 'RSS 2026 · Robot World Model Workshop',
    authors: 'Devesh Nath*, Anutam Srinivasan*, Haoran Yin*, Ruitong Jiang, Jeffrey Fang, Glen Chou',
    description: 'Turning raw pixels into probabilistically safe robot control by combining learned latent world models, calibrated uncertainty, and GPU-parallel robust MPC.',
    topics: ['Pixels to Safe Control', 'Conformalized World Models', 'GPU-Parallel Robust MPC', 'Safe Vision-Based Manipulation'],
  },
  {
    slug: 'koopman-reachability',
    year: 2026,
    paperUrl: 'https://arxiv.org/pdf/2601.01076',
    videoUrl: '#', // Replace with the YouTube URL.
    media: { src: '/projects/koopman-reachability/assets/thumbnail.mp4', type: 'video' },
    title: 'Scalable Data-Driven Reachability Analysis and Control via Koopman Operators with Conformal Coverage Guarantees',
    venue: 'L4DC 2026',
    distinction: 'Best Paper Finalist',
    authors: 'Devesh Nath*, Haoran Yin*, Glen Chou',
    description: 'Scaling probabilistically guaranteed safety verification to high-dimensional nonlinear robotics by combining learned Koopman dynamics, efficient reachability analysis, and conformal prediction.',
    topics: ['Scalable Nonlinear Reachability', 'Conformal Safety Guarantees', 'Learned Koopman Linearization', 'Black Box Dynamics'],
  },
  {
    slug: 'micrompc',
    year: 2027,
    paperUrl: '#', // Replace with the arXiv URL.
    videoUrl: '#', // Replace with the YouTube URL.
    media: { src: '/projects/micrompc/assets/thumbnail.mp4', type: 'video' },
    title: 'μMPC: Safe Nonlinear and World Model Control in Microseconds via Koopman-Linearized Pre-Compilation',
    venue: 'ICRA 2027 · In Submission',
    authors: 'Devesh Nath, Glen Chou',
    description: 'Enabling microsecond scale nonlinear robotic planning. Applied for sub-millisecond vision-based planning with linear world models and fast, efficient high-dimensional robot control.',
    topics: ['Scalable Nonlinear Optimal Control', 'Fast Unitree Go2 Control', 'Real-time Control with World Models', 'Highly Scalable Multi-Agent Planning'],
  },
  {
    slug: 'generative-planner-safety',
    year: 2026,
    paperUrl: '#', // Replace with the arXiv URL.
    videoUrl: '#', // Replace with the YouTube URL.
    media: null, // Set to { src: '/media/example.mp4', type: 'video' } or type: 'image'.
    title: 'Formal Safety Verification and Refinement for Generative Motion Planners via Certified Local Stabilization',
    venue: 'ICRA 2026',
    authors: 'Devesh Nath*, Haoran Yin*, Glen Chou',
    description: 'Bringing formal safety guarantees to diffusion, flow-matching, and vision-language motion planners through certified local stabilization, preserving multimodal behavior without retraining the generative models.',
    topics: ['Formally Verified Generative Planning', 'Safe Multimodal Planning', 'Certified Local Stabilization', 'Retraining-Free Safety Refinement'],
  },
  {
    slug: 'adaptive-conformal-prediction',
    year: 2027,
    paperUrl: '#', // Replace with the arXiv URL.
    videoUrl: '#', // Replace with the YouTube URL.
    media: null, // Set to { src: '/media/example.mp4', type: 'video' } or type: 'image'.
    title: 'Adaptive Conformal Prediction Via Learned Residual-Law Retrieval',
    venue: 'ICLR 2027 · In Submission',
    authors: 'Devesh Nath, Rahul Rustagi, Glen Chou',
    description: 'Scaling conformal prediction to high-dimensional statistical inference, with applications to multimodal trajectory uncertainty in autonomous driving and long horizon robot reachability.',
    topics: ['Scalable Conformal Prediction', 'Learned Uncertainty Representation', 'Conformal Multimodal Autonomous Driving', 'High Dimensional Reachability'],
  },
];
