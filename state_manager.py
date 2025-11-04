"""
🛰️ SPACE MISSION STATE MANAGEMENT
Advanced state management for autonomous space mission planning
"""

from typing import Dict, List, Any, Optional, TypedDict, Union
from datetime import datetime, timedelta
import json
import asyncio
import logging
from dataclasses import dataclass, asdict
from enum import Enum
import uuid

logger = logging.getLogger(__name__)

class MissionPhase(Enum):
    """Mission phases"""
    INITIALIZATION = "initialization"
    ORBITAL_CALCULATION = "orbital_calculation"
    CONSTELLATION_MANAGEMENT = "constellation_management"
    COLLISION_MONITORING = "collision_monitoring"
    MISSION_PLANNING = "mission_planning"
    GROUND_COORDINATION = "ground_coordination"
    MAINTENANCE_ANALYSIS = "maintenance_analysis"
    DEBRIS_MONITORING = "debris_monitoring"
    COMPLETED = "completed"
    ERROR = "error"

class AlertLevel(Enum):
    """Alert severity levels"""
    INFO = "info"
    WARNING = "warning"
    HIGH = "high"
    CRITICAL = "critical"

class SatelliteStatus(Enum):
    """Satellite operational status"""
    ACTIVE = "active"
    STANDBY = "standby"
    MAINTENANCE = "maintenance"
    OFFLINE = "offline"
    EMERGENCY = "emergency"

@dataclass
class Satellite:
    """Satellite data structure with comprehensive state"""
    id: str
    name: str
    type: str
    status: SatelliteStatus
    altitude: float  # km
    inclination: float  # degrees
    longitude: float  # degrees
    latitude: float  # degrees
    velocity: float  # km/s
    battery_level: float  # percentage
    signal_strength: float  # percentage
    temperature: float  # Celsius
    power_consumption: float  # Watts
    data_throughput: float  # Mbps
    last_contact: str
    health_score: float  # 0-100
    maintenance_due: bool
    collision_risk: float  # 0-1

@dataclass
class OrbitalData:
    """Orbital mechanics data"""
    satellite_id: str
    position: List[float]  # [x, y, z] in km
    velocity: List[float]  # [vx, vy, vz] in km/s
    acceleration: List[float]  # [ax, ay, az] in km/s²
    orbital_period: float  # seconds
    eccentricity: float
    inclination: float  # degrees
    right_ascension: float  # degrees
    argument_of_perigee: float  # degrees
    mean_anomaly: float  # degrees
    timestamp: str

@dataclass
class CollisionThreat:
    """Collision threat data"""
    threat_id: str
    satellite_1: str
    satellite_2: str
    distance: float  # km
    time_to_collision: float  # hours
    risk_level: str
    avoidance_maneuver: str
    confidence: float  # 0-1
    timestamp: str

@dataclass
class GroundStation:
    """Ground station data"""
    id: str
    name: str
    location: str
    coordinates: List[float]  # [lat, lon]
    status: str
    satellites_connected: List[str]
    data_rate: float  # Gbps
    antenna_diameter: float  # meters
    frequency_band: str
    last_contact: str

@dataclass
class SpaceDebris:
    """Space debris object data"""
    id: str
    name: str
    size: str
    mass: float  # kg
    velocity: float  # km/s
    orbit_altitude: float  # km
    threat_level: str
    tracking_accuracy: float  # percentage
    last_updated: str

@dataclass
class MaintenanceTask:
    """Maintenance task data"""
    task_id: str
    satellite_id: str
    task_type: str
    priority: str
    estimated_duration: float  # hours
    required_resources: List[str]
    scheduled_time: str
    status: str
    confidence: float  # 0-1

@dataclass
class Alert:
    """Alert data"""
    alert_id: str
    type: str
    level: AlertLevel
    message: str
    satellite_id: Optional[str]
    timestamp: str
    acknowledged: bool
    resolved: bool

@dataclass
class Decision:
    """Agent decision data"""
    decision_id: str
    agent: str
    decision: str
    reasoning: str
    confidence: float  # 0-1
    timestamp: str
    impact: str

class SpaceMissionState(TypedDict):
    """Comprehensive state management for space mission agent"""
    # Mission metadata
    mission_id: str
    mission_name: str
    mission_phase: MissionPhase
    start_time: str
    last_update: str
    
    # Satellite constellation
    satellites: List[Dict[str, Any]]
    satellite_count: int
    
    # Orbital mechanics
    orbital_data: List[Dict[str, Any]]
    trajectory_predictions: List[Dict[str, Any]]
    
    # Collision avoidance
    collision_threats: List[Dict[str, Any]]
    avoidance_maneuvers: List[Dict[str, Any]]
    
    # Mission planning
    mission_plan: Dict[str, Any]
    objectives: List[str]
    timeline: Dict[str, Any]
    resources: Dict[str, Any]
    
    # Ground stations
    ground_stations: List[Dict[str, Any]]
    communication_links: List[Dict[str, Any]]
    
    # Maintenance
    maintenance_schedule: Dict[str, Any]
    maintenance_tasks: List[Dict[str, Any]]
    health_monitoring: Dict[str, Any]
    
    # Space debris
    space_debris: List[Dict[str, Any]]
    debris_threats: List[Dict[str, Any]]
    
    # System state
    alerts: List[Dict[str, Any]]
    decisions: List[Dict[str, Any]]
    performance_metrics: Dict[str, Any]
    system_health: Dict[str, Any]
    
    # Error handling
    errors: List[Dict[str, Any]]
    recovery_actions: List[Dict[str, Any]]

class StateManager:
    """
    🛰️ ADVANCED STATE MANAGER FOR SPACE MISSION AGENT
    
    Manages complex state for autonomous space mission planning,
    satellite constellation management, and real-time decision making.
    """
    
    def __init__(self):
        self.state: SpaceMissionState = self._initialize_state()
        self.state_history: List[SpaceMissionState] = []
        self.max_history_size = 100
        
    def _initialize_state(self) -> SpaceMissionState:
        """Initialize the space mission state"""
        return SpaceMissionState(
            # Mission metadata
            mission_id=str(uuid.uuid4()),
            mission_name="Autonomous Space Mission",
            mission_phase=MissionPhase.INITIALIZATION,
            start_time=datetime.now().isoformat(),
            last_update=datetime.now().isoformat(),
            
            # Satellite constellation
            satellites=[],
            satellite_count=0,
            
            # Orbital mechanics
            orbital_data=[],
            trajectory_predictions=[],
            
            # Collision avoidance
            collision_threats=[],
            avoidance_maneuvers=[],
            
            # Mission planning
            mission_plan={},
            objectives=[],
            timeline={},
            resources={},
            
            # Ground stations
            ground_stations=[],
            communication_links=[],
            
            # Maintenance
            maintenance_schedule={},
            maintenance_tasks=[],
            health_monitoring={},
            
            # Space debris
            space_debris=[],
            debris_threats=[],
            
            # System state
            alerts=[],
            decisions=[],
            performance_metrics={},
            system_health={},
            
            # Error handling
            errors=[],
            recovery_actions=[]
        )
    
    def update_mission_phase(self, phase: MissionPhase) -> None:
        """Update the current mission phase"""
        self.state["mission_phase"] = phase
        self.state["last_update"] = datetime.now().isoformat()
        logger.info(f"🛰️ Mission phase updated to: {phase.value}")
    
    def add_satellite(self, satellite: Satellite) -> None:
        """Add a satellite to the constellation"""
        satellite_dict = asdict(satellite)
        satellite_dict["status"] = satellite.status.value
        self.state["satellites"].append(satellite_dict)
        self.state["satellite_count"] = len(self.state["satellites"])
        self.state["last_update"] = datetime.now().isoformat()
        logger.info(f"🛰️ Added satellite: {satellite.id}")
    
    def update_satellite(self, satellite_id: str, updates: Dict[str, Any]) -> None:
        """Update satellite data"""
        for satellite in self.state["satellites"]:
            if satellite["id"] == satellite_id:
                satellite.update(updates)
                satellite["last_contact"] = datetime.now().isoformat()
                break
        self.state["last_update"] = datetime.now().isoformat()
        logger.info(f"🛰️ Updated satellite: {satellite_id}")
    
    def add_orbital_data(self, orbital_data: OrbitalData) -> None:
        """Add orbital mechanics data"""
        orbital_dict = asdict(orbital_data)
        self.state["orbital_data"].append(orbital_dict)
        self.state["last_update"] = datetime.now().isoformat()
        logger.info(f"🛰️ Added orbital data for: {orbital_data.satellite_id}")
    
    def add_collision_threat(self, threat: CollisionThreat) -> None:
        """Add collision threat"""
        threat_dict = asdict(threat)
        self.state["collision_threats"].append(threat_dict)
        self.state["last_update"] = datetime.now().isoformat()
        logger.warning(f"🚨 Collision threat detected: {threat.threat_id}")
    
    def add_ground_station(self, station: GroundStation) -> None:
        """Add ground station"""
        station_dict = asdict(station)
        self.state["ground_stations"].append(station_dict)
        self.state["last_update"] = datetime.now().isoformat()
        logger.info(f"🌍 Added ground station: {station.id}")
    
    def add_space_debris(self, debris: SpaceDebris) -> None:
        """Add space debris object"""
        debris_dict = asdict(debris)
        self.state["space_debris"].append(debris_dict)
        self.state["last_update"] = datetime.now().isoformat()
        logger.info(f"🗑️ Added space debris: {debris.id}")
    
    def add_maintenance_task(self, task: MaintenanceTask) -> None:
        """Add maintenance task"""
        task_dict = asdict(task)
        self.state["maintenance_tasks"].append(task_dict)
        self.state["last_update"] = datetime.now().isoformat()
        logger.info(f"🔧 Added maintenance task: {task.task_id}")
    
    def add_alert(self, alert: Alert) -> None:
        """Add system alert"""
        alert_dict = asdict(alert)
        alert_dict["level"] = alert.level.value
        self.state["alerts"].append(alert_dict)
        self.state["last_update"] = datetime.now().isoformat()
        logger.warning(f"⚠️ Alert: {alert.message}")
    
    def add_decision(self, decision: Decision) -> None:
        """Add agent decision"""
        decision_dict = asdict(decision)
        self.state["decisions"].append(decision_dict)
        self.state["last_update"] = datetime.now().isoformat()
        logger.info(f"🤖 Decision: {decision.decision}")
    
    def update_performance_metrics(self, metrics: Dict[str, Any]) -> None:
        """Update performance metrics"""
        self.state["performance_metrics"].update(metrics)
        self.state["last_update"] = datetime.now().isoformat()
        logger.info(f"📊 Updated performance metrics")
    
    def update_system_health(self, health: Dict[str, Any]) -> None:
        """Update system health status"""
        self.state["system_health"].update(health)
        self.state["last_update"] = datetime.now().isoformat()
        logger.info(f"🏥 Updated system health")
    
    def save_state_snapshot(self) -> None:
        """Save current state as snapshot"""
        snapshot = self.state.copy()
        self.state_history.append(snapshot)
        
        # Maintain history size limit
        if len(self.state_history) > self.max_history_size:
            self.state_history.pop(0)
        
        logger.info(f"💾 State snapshot saved (history: {len(self.state_history)})")
    
    def get_state_summary(self) -> Dict[str, Any]:
        """Get comprehensive state summary"""
        return {
            "mission_id": self.state["mission_id"],
            "mission_phase": self.state["mission_phase"].value,
            "satellite_count": self.state["satellite_count"],
            "collision_threats": len(self.state["collision_threats"]),
            "ground_stations": len(self.state["ground_stations"]),
            "space_debris": len(self.state["space_debris"]),
            "maintenance_tasks": len(self.state["maintenance_tasks"]),
            "alerts": len(self.state["alerts"]),
            "decisions": len(self.state["decisions"]),
            "last_update": self.state["last_update"],
            "system_health": self.state["system_health"],
            "performance_metrics": self.state["performance_metrics"]
        }
    
    def get_satellite_by_id(self, satellite_id: str) -> Optional[Dict[str, Any]]:
        """Get satellite by ID"""
        for satellite in self.state["satellites"]:
            if satellite["id"] == satellite_id:
                return satellite
        return None
    
    def get_active_alerts(self) -> List[Dict[str, Any]]:
        """Get active (unresolved) alerts"""
        return [alert for alert in self.state["alerts"] if not alert.get("resolved", False)]
    
    def get_high_priority_tasks(self) -> List[Dict[str, Any]]:
        """Get high priority maintenance tasks"""
        return [task for task in self.state["maintenance_tasks"] 
                if task.get("priority") == "HIGH" and task.get("status") != "completed"]
    
    def get_collision_risks(self) -> List[Dict[str, Any]]:
        """Get high-risk collision threats"""
        return [threat for threat in self.state["collision_threats"] 
                if threat.get("risk_level") in ["HIGH", "CRITICAL"]]
    
    def export_state(self) -> str:
        """Export state as JSON"""
        export_data = self.state.copy()
        export_data["mission_phase"] = self.state["mission_phase"].value
        return json.dumps(export_data, indent=2, default=str)
    
    def import_state(self, state_data: str) -> None:
        """Import state from JSON"""
        imported_state = json.loads(state_data)
        self.state.update(imported_state)
        self.state["last_update"] = datetime.now().isoformat()
        logger.info("📥 State imported successfully")
    
    def reset_state(self) -> None:
        """Reset state to initial values"""
        self.state = self._initialize_state()
        self.state_history.clear()
        logger.info("🔄 State reset to initial values")
    
    def get_state_history(self) -> List[Dict[str, Any]]:
        """Get state history"""
        return [state.copy() for state in self.state_history]
    
    def get_mission_timeline(self) -> Dict[str, Any]:
        """Get mission timeline"""
        return {
            "start_time": self.state["start_time"],
            "current_phase": self.state["mission_phase"].value,
            "last_update": self.state["last_update"],
            "duration": self._calculate_mission_duration(),
            "phases_completed": len([phase for phase in MissionPhase if phase != self.state["mission_phase"]]),
            "total_phases": len(MissionPhase)
        }
    
    def _calculate_mission_duration(self) -> str:
        """Calculate mission duration"""
        start_time = datetime.fromisoformat(self.state["start_time"])
        current_time = datetime.now()
        duration = current_time - start_time
        return str(duration)

# Example usage
async def main():
    """Example of using the state manager"""
    
    state_manager = StateManager()
    
    # Create sample satellite
    satellite = Satellite(
        id="SAT-001",
        name="Communication Satellite Alpha",
        type="Communication",
        status=SatelliteStatus.ACTIVE,
        altitude=400,
        inclination=51.6,
        longitude=-180,
        latitude=0,
        velocity=7.5,
        battery_level=85,
        signal_strength=95,
        temperature=20,
        power_consumption=1000,
        data_throughput=100,
        last_contact=datetime.now().isoformat(),
        health_score=95,
        maintenance_due=False,
        collision_risk=0.01
    )
    
    # Add satellite to state
    state_manager.add_satellite(satellite)
    
    # Update mission phase
    state_manager.update_mission_phase(MissionPhase.ORBITAL_CALCULATION)
    
    # Add orbital data
    orbital_data = OrbitalData(
        satellite_id="SAT-001",
        position=[6371 + 400, 0, 0],
        velocity=[0, 7.5, 0],
        acceleration=[0, 0, 0],
        orbital_period=5400,
        eccentricity=0.001,
        inclination=51.6,
        right_ascension=0,
        argument_of_perigee=0,
        mean_anomaly=0,
        timestamp=datetime.now().isoformat()
    )
    state_manager.add_orbital_data(orbital_data)
    
    # Add alert
    alert = Alert(
        alert_id="ALT-001",
        type="SYSTEM_HEALTH",
        level=AlertLevel.INFO,
        message="Satellite health monitoring active",
        satellite_id="SAT-001",
        timestamp=datetime.now().isoformat(),
        acknowledged=False,
        resolved=False
    )
    state_manager.add_alert(alert)
    
    # Add decision
    decision = Decision(
        decision_id="DEC-001",
        agent="orbital_mechanics",
        decision="Calculated optimal orbital trajectory",
        reasoning="Based on mission objectives and constraints",
        confidence=0.95,
        timestamp=datetime.now().isoformat(),
        impact="Improved mission efficiency"
    )
    state_manager.add_decision(decision)
    
    # Save state snapshot
    state_manager.save_state_snapshot()
    
    # Get state summary
    summary = state_manager.get_state_summary()
    print("🛰️ State Summary:")
    print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    asyncio.run(main())
