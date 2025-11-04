"""
🚀 SPACE MISSION AGENT TESTING
Comprehensive testing for the space mission agent
"""

import asyncio
import pytest
import json
from datetime import datetime
from unittest.mock import Mock, patch
import logging

# Import our modules
from main_agent import AutonomousSpaceMissionAgent
from state_manager import StateManager, MissionPhase, AlertLevel, Satellite, SatelliteStatus
from local_tools import SpaceMissionTools
from agent_graph import SpaceMissionAgent

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestSpaceMissionAgent:
    """Test suite for the space mission agent"""
    
    @pytest.fixture
    def agent(self):
        """Create test agent instance"""
        with patch.dict('os.environ', {'OPENAI_API_KEY': 'test-key'}):
            return AutonomousSpaceMissionAgent()
    
    @pytest.fixture
    def sample_satellites(self):
        """Create sample satellites for testing"""
        return [
            Satellite(
                id="SAT-001",
                name="Test Satellite Alpha",
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
            ),
            Satellite(
                id="SAT-002",
                name="Test Satellite Beta",
                type="Navigation",
                status=SatelliteStatus.ACTIVE,
                altitude=450,
                inclination=55.0,
                longitude=-120,
                latitude=10,
                velocity=7.3,
                battery_level=90,
                signal_strength=98,
                temperature=18,
                power_consumption=1200,
                data_throughput=150,
                last_contact=datetime.now().isoformat(),
                health_score=98,
                maintenance_due=False,
                collision_risk=0.02
            )
        ]
    
    @pytest.mark.asyncio
    async def test_agent_initialization(self, agent):
        """Test agent initialization"""
        assert agent is not None
        assert agent.state_manager is not None
        assert agent.tools is not None
        assert agent.agent is not None
        logger.info("✅ Agent initialization test passed")
    
    @pytest.mark.asyncio
    async def test_mission_initialization(self, agent):
        """Test mission initialization"""
        result = await agent.initialize_mission("Test Mission")
        
        assert result is not None
        assert "satellite_count" in result
        assert result["satellite_count"] > 0
        assert result["mission_phase"] == MissionPhase.INITIALIZATION.value
        logger.info("✅ Mission initialization test passed")
    
    @pytest.mark.asyncio
    async def test_satellite_management(self, agent, sample_satellites):
        """Test satellite management functionality"""
        # Add satellites
        for satellite in sample_satellites:
            agent.state_manager.add_satellite(satellite)
        
        # Test satellite retrieval
        satellite = agent.state_manager.get_satellite_by_id("SAT-001")
        assert satellite is not None
        assert satellite["id"] == "SAT-001"
        
        # Test satellite count
        assert agent.state_manager.state["satellite_count"] == 2
        logger.info("✅ Satellite management test passed")
    
    @pytest.mark.asyncio
    async def test_orbital_mechanics_calculation(self, agent):
        """Test orbital mechanics calculations"""
        tools = SpaceMissionTools()
        
        # Create test satellite
        satellite = Satellite(
            id="TEST-SAT",
            name="Test Satellite",
            type="Test",
            status=SatelliteStatus.ACTIVE,
            altitude=400,
            inclination=51.6,
            longitude=0,
            latitude=0,
            velocity=7.5,
            battery_level=100,
            signal_strength=100,
            temperature=20,
            power_consumption=1000,
            data_throughput=100,
            last_contact=datetime.now().isoformat(),
            health_score=100,
            maintenance_due=False,
            collision_risk=0.0
        )
        
        # Calculate orbital mechanics
        position = await tools.calculate_orbital_mechanics(satellite)
        
        assert position is not None
        assert hasattr(position, 'x')
        assert hasattr(position, 'y')
        assert hasattr(position, 'z')
        assert hasattr(position, 'velocity_x')
        assert hasattr(position, 'velocity_y')
        assert hasattr(position, 'velocity_z')
        logger.info("✅ Orbital mechanics calculation test passed")
    
    @pytest.mark.asyncio
    async def test_collision_threat_detection(self, agent, sample_satellites):
        """Test collision threat detection"""
        tools = SpaceMissionTools()
        
        # Detect collision threats
        threats = await tools.detect_collision_threats(sample_satellites)
        
        assert isinstance(threats, list)
        logger.info(f"✅ Collision threat detection test passed - {len(threats)} threats detected")
    
    @pytest.mark.asyncio
    async def test_constellation_optimization(self, agent, sample_satellites):
        """Test constellation optimization"""
        tools = SpaceMissionTools()
        
        # Optimize constellation
        optimization = await tools.optimize_constellation_coverage(sample_satellites)
        
        assert optimization is not None
        assert "total_satellites" in optimization
        assert "coverage_percentage" in optimization
        assert optimization["total_satellites"] == len(sample_satellites)
        logger.info("✅ Constellation optimization test passed")
    
    @pytest.mark.asyncio
    async def test_predictive_maintenance(self, agent, sample_satellites):
        """Test predictive maintenance"""
        tools = SpaceMissionTools()
        
        # Predict maintenance
        maintenance = await tools.predict_satellite_maintenance(sample_satellites)
        
        assert isinstance(maintenance, list)
        logger.info(f"✅ Predictive maintenance test passed - {len(maintenance)} maintenance predictions")
    
    @pytest.mark.asyncio
    async def test_space_debris_monitoring(self, agent):
        """Test space debris monitoring"""
        tools = SpaceMissionTools()
        
        # Monitor space debris
        debris = await tools.monitor_space_debris()
        
        assert isinstance(debris, list)
        assert len(debris) > 0
        logger.info(f"✅ Space debris monitoring test passed - {len(debris)} debris objects")
    
    @pytest.mark.asyncio
    async def test_ground_station_coordination(self, agent, sample_satellites):
        """Test ground station coordination"""
        tools = SpaceMissionTools()
        
        # Coordinate ground stations
        stations = await tools.coordinate_ground_stations(sample_satellites)
        
        assert isinstance(stations, list)
        assert len(stations) > 0
        logger.info(f"✅ Ground station coordination test passed - {len(stations)} stations")
    
    @pytest.mark.asyncio
    async def test_mission_report_generation(self, agent):
        """Test mission report generation"""
        tools = SpaceMissionTools()
        
        # Create sample mission data
        mission_data = {
            "mission_id": "TEST-001",
            "satellites": [{"id": "SAT-001", "status": "Active"}],
            "collision_threats": [],
            "maintenance_schedule": {"maintenance_required": []},
            "space_debris": [],
            "ground_stations": [],
            "alerts": [],
            "decisions": []
        }
        
        # Generate mission report
        report = await tools.generate_mission_report(mission_data)
        
        assert report is not None
        assert "mission_id" in report
        assert "performance_metrics" in report
        logger.info("✅ Mission report generation test passed")
    
    @pytest.mark.asyncio
    async def test_state_management(self, agent):
        """Test state management functionality"""
        state_manager = agent.state_manager
        
        # Test state initialization
        assert state_manager.state is not None
        assert "mission_id" in state_manager.state
        
        # Test state update
        state_manager.update_mission_phase(MissionPhase.ORBITAL_CALCULATION)
        assert state_manager.state["mission_phase"] == MissionPhase.ORBITAL_CALCULATION
        
        # Test state summary
        summary = state_manager.get_state_summary()
        assert summary is not None
        assert "mission_phase" in summary
        logger.info("✅ State management test passed")
    
    @pytest.mark.asyncio
    async def test_alert_system(self, agent):
        """Test alert system"""
        from state_manager import Alert
        
        # Create test alert
        alert = Alert(
            alert_id="TEST-001",
            type="TEST_ALERT",
            level=AlertLevel.INFO,
            message="Test alert message",
            satellite_id="SAT-001",
            timestamp=datetime.now().isoformat(),
            acknowledged=False,
            resolved=False
        )
        
        # Add alert
        agent.state_manager.add_alert(alert)
        
        # Test alert retrieval
        alerts = agent.state_manager.get_active_alerts()
        assert len(alerts) > 0
        assert alerts[0]["alert_id"] == "TEST-001"
        logger.info("✅ Alert system test passed")
    
    @pytest.mark.asyncio
    async def test_decision_tracking(self, agent):
        """Test decision tracking"""
        from state_manager import Decision
        
        # Create test decision
        decision = Decision(
            decision_id="DEC-001",
            agent="test_agent",
            decision="Test decision",
            reasoning="Test reasoning",
            confidence=0.95,
            timestamp=datetime.now().isoformat(),
            impact="Test impact"
        )
        
        # Add decision
        agent.state_manager.add_decision(decision)
        
        # Test decision retrieval
        decisions = agent.state_manager.state["decisions"]
        assert len(decisions) > 0
        assert decisions[0]["decision_id"] == "DEC-001"
        logger.info("✅ Decision tracking test passed")
    
    @pytest.mark.asyncio
    async def test_performance_metrics(self, agent):
        """Test performance metrics"""
        # Update performance metrics
        metrics = {
            "uptime": "99.9%",
            "coverage": "99.8%",
            "latency": "< 50ms",
            "collision_risk": "< 0.1%"
        }
        
        agent.state_manager.update_performance_metrics(metrics)
        
        # Test metrics retrieval
        assert agent.state_manager.state["performance_metrics"]["uptime"] == "99.9%"
        assert agent.state_manager.state["performance_metrics"]["coverage"] == "99.8%"
        logger.info("✅ Performance metrics test passed")
    
    @pytest.mark.asyncio
    async def test_export_import(self, agent):
        """Test state export and import"""
        # Export state
        exported_state = agent.state_manager.export_state()
        assert exported_state is not None
        assert isinstance(exported_state, str)
        
        # Import state
        agent.state_manager.import_state(exported_state)
        assert agent.state_manager.state is not None
        logger.info("✅ Export/import test passed")
    
    @pytest.mark.asyncio
    async def test_full_mission_simulation(self, agent):
        """Test full mission simulation"""
        # Initialize mission
        init_result = await agent.initialize_mission("Test Mission")
        assert init_result is not None
        
        # Get mission status
        status = await agent.get_mission_status()
        assert status is not None
        assert "satellite_count" in status
        
        # Test mission data export
        mission_data = await agent.export_mission_data()
        assert mission_data is not None
        assert isinstance(mission_data, str)
        
        logger.info("✅ Full mission simulation test passed")

# Run tests
async def run_all_tests():
    """Run all tests"""
    logger.info("🚀 Starting Space Mission Agent Tests...")
    
    # Create test instance
    test_suite = TestSpaceMissionAgent()
    
    # Run individual tests
    tests = [
        test_suite.test_agent_initialization,
        test_suite.test_mission_initialization,
        test_suite.test_satellite_management,
        test_suite.test_orbital_mechanics_calculation,
        test_suite.test_collision_threat_detection,
        test_suite.test_constellation_optimization,
        test_suite.test_predictive_maintenance,
        test_suite.test_space_debris_monitoring,
        test_suite.test_ground_station_coordination,
        test_suite.test_mission_report_generation,
        test_suite.test_state_management,
        test_suite.test_alert_system,
        test_suite.test_decision_tracking,
        test_suite.test_performance_metrics,
        test_suite.test_export_import,
        test_suite.test_full_mission_simulation
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            await test()
            passed += 1
            logger.info(f"✅ {test.__name__} PASSED")
        except Exception as e:
            failed += 1
            logger.error(f"❌ {test.__name__} FAILED: {str(e)}")
    
    logger.info(f"🚀 Test Results: {passed} passed, {failed} failed")
    
    if failed == 0:
        logger.info("🎉 ALL TESTS PASSED! The space mission agent is ready!")
    else:
        logger.warning(f"⚠️ {failed} tests failed. Please review and fix issues.")

if __name__ == "__main__":
    asyncio.run(run_all_tests())
