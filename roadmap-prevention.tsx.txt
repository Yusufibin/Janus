import React from 'react';

const RoadmapStep = ({ number, title, color, description, isLeft }) => (
  <div className={`flex ${isLeft ? 'flex-row' : 'flex-row-reverse'} items-center gap-4 w-full my-8`}>
    <div className={`flex-1 ${isLeft ? 'text-right' : 'text-left'}`}>
      <div className={`inline-flex items-center justify-center w-16 h-16 rounded-full ${color} text-white font-bold text-xl shadow-lg`}>
        {number}
      </div>
      <h3 className="text-xl font-bold mt-2 mb-1">{title}</h3>
      <p className="text-gray-600 text-sm">{description}</p>
    </div>
    <div className="w-24 relative">
      <div className="absolute top-8 w-full h-2 bg-gray-300"></div>
    </div>
    <div className="flex-1"></div>
  </div>
);

const Roadmap = () => {
  const steps = [
    {
      number: "01",
      title: "Consultation Médicale",
      color: "bg-emerald-500",
      description: "Privilégier la consultation d'un professionnel de santé pour un diagnostic précis",
      isLeft: true
    },
    {
      number: "02",
      title: "Circuits Légaux",
      color: "bg-blue-500",
      description: "Acheter les médicaments uniquement dans les pharmacies autorisées",
      isLeft: false
    },
    {
      number: "03",
      title: "Éducation & Sensibilisation",
      color: "bg-purple-500",
      description: "Renforcer les campagnes d'information sur les risques de l'automédication",
      isLeft: true
    },
    {
      number: "04",
      title: "Systèmes de Santé",
      color: "bg-orange-500",
      description: "Améliorer l'accès aux soins et la qualité des services de santé",
      isLeft: false
    },
    {
      number: "05",
      title: "Réglementation",
      color: "bg-pink-500",
      description: "Encadrer la publicité et lutter contre le marché illégal des médicaments",
      isLeft: true
    }
  ];

  return (
    <div className="max-w-4xl mx-auto p-8 bg-white rounded-xl shadow-lg">
      <h2 className="text-2xl font-bold text-center mb-12">Roadmap de Prévention de l'Automédication</h2>
      <div className="relative">
        {steps.map((step, index) => (
          <RoadmapStep key={index} {...step} />
        ))}
        <div className="absolute top-0 left-1/2 w-2 h-full bg-gray-300 -translate-x-1/2 -z-10">
          <div className="absolute top-0 left-1/2 w-4 h-4 bg-emerald-500 rounded-full -translate-x-1/2"></div>
          <div className="absolute bottom-0 left-1/2 w-4 h-4 bg-pink-500 rounded-full -translate-x-1/2"></div>
        </div>
      </div>
    </div>
  );
};

export default Roadmap;
