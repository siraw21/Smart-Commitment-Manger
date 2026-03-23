import { useEffect, useState } from "react";
import { getTasks, generatePlan } from "../services/api";

export default function Dashboard() {
  const [tasks, setTasks] = useState([]);
  const [plan, setPlan] = useState([]);
  const [energy, setEnergy] = useState("medium");

  useEffect(() => {
    loadTasks();
  }, []);

  const loadTasks = async () => {
    const data = await getTasks();
    setTasks(data);
  };

  const handleGeneratePlan = async () => {
    const data = await generatePlan({
      available_minutes: 120,
      energy_level: energy,
    });
    setPlan(data);
  };

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <h1 className="text-2xl font-bold mb-4">Smart Commitment Manager</h1>

      {/* Energy Selector */}
      <div className="mb-4">
        <label className="mr-2">Energy Level:</label>
        <select
          value={energy}
          onChange={(e) => setEnergy(e.target.value)}
          className="p-2 border rounded"
        >
          <option value="low">Low</option>
          <option value="medium">Medium</option>
          <option value="high">High</option>
        </select>
      </div>

      {/* Generate Plan Button */}
      <button
        onClick={handleGeneratePlan}
        className="bg-blue-500 text-white px-4 py-2 rounded"
      >
        Generate Plan
      </button>

      {/* Plan Output */}
      <div className="mt-6">
        <h2 className="text-xl font-semibold">Today's Plan</h2>

        {plan.map((task, index) => (
          <div key={index} className="bg-white p-4 mt-2 rounded shadow">
            <p className="font-bold">{task.title}</p>
            <p>Time: {task.estimated_time} min</p>
          </div>
        ))}
      </div>
    </div>
  );
}
