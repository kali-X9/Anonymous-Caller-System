# 🔒 Anonymous Caller System

*A sophisticated, enterprise-grade anonymous communication platform designed for maximum operational security and untraceable voice communications.*

---

## 📖 Table of Contents

- [Overview](#overview)
- [Security Architecture](#security-architecture)
- [Core Features](#core-features)
- [System Requirements](#system-requirements)
- [Installation Guide](#installation-guide)
- [Configuration](#configuration)
- [Usage Examples](#usage-examples)
- [Docker Deployment](#docker-deployment)
- [Performance Optimization](#performance-optimization)
- [Logging & Monitoring](#logging--monitoring)
- [Security Considerations](#security-considerations)
- [Testing Framework](#testing-framework)
- [CI/CD Integration](#cicd-integration)
- [Directory Structure](#directory-structure)
- [Troubleshooting](#troubleshooting)
- [Version History](#version-history)
- [License](#license)

---

## 🔍 Overview

This repository contains a comprehensive anonymous calling system engineered for penetration testers, security researchers, and privacy-focused professionals who require completely untraceable voice communications. The system implements multiple layers of obfuscation including Tor networking, MAC address spoofing, dynamic IP rotation, and encrypted SIP protocol communications.

Built with production-grade architecture principles, this tool follows enterprise security standards while maintaining operational simplicity. The modular design allows for easy extension and integration with existing security frameworks.

**Warning**: This tool is intended for legitimate security research and authorized penetration testing activities only. Unauthorized use may violate local laws and regulations.

---

## 🛡️ Security Architecture

The system employs a multi-layered security approach:

### Network Layer Protection
- **Tor Integration**: All network traffic routed through the Tor network for anonymization
- **Dynamic IP Rotation**: Automatic IP address changes at configurable intervals
- **MAC Address Spoofing**: Hardware identification obfuscation
- **VPN Tunneling**: Additional network layer encryption and routing

### Communication Layer Security
- **SIP Encryption**: Secure Session Initiation Protocol implementation
- **End-to-End Encryption**: Voice data protected during transmission
- **Authentication Hardening**: Strong credential management and validation

### Application Layer Defenses
- **Input Sanitization**: Comprehensive parameter validation
- **Exception Handling**: Graceful error management without information leakage
- **Resource Isolation**: Process sandboxing and privilege separation
- **Audit Trail**: Complete operational logging with rotation

---

## ⭐ Core Features

### Real-Time Anonymity Engine
- Automated Tor service management
- Dynamic IP address rotation every 10 seconds
- Concurrent network stack manipulation
- Asynchronous operation for optimal performance

### Advanced Network Obfuscation
- MAC address randomization with hardware-level spoofing
- Interface state management for seamless transitions
- Network interface monitoring and recovery

### Secure Voice Communications
- SIP protocol implementation with military-grade encryption
- Incoming call auto-answer capabilities
- Configurable authentication parameters
- Call session management and cleanup

### Enterprise Infrastructure
- Modular component architecture
- YAML-based configuration management
- Structured logging with file rotation
- Health check and status monitoring
- Comprehensive exception handling framework

### Development Operations
- Automated dependency resolution
- Virtual environment isolation
- Container-ready deployment
- Continuous integration pipeline
- Unit testing framework

---

## 💻 System Requirements

### Operating System
- **Primary Support**: Kali Linux Rolling Release
- **Secondary Support**: Ubuntu 20.04+, Debian 11+
- **Architecture**: x86_64, ARM64

### Hardware Specifications
- **Minimum RAM**: 4GB
- **Recommended RAM**: 8GB+
- **Storage**: 500MB free space
- **Network**: Ethernet interface recommended

### Software Dependencies
- Python 3.9 or higher
- Tor service daemon
- OpenVPN client
- MacChanger utility
- PJSIP library
- Systemd or equivalent init system

### Privileges Required
- Root/Administrator access for network interface manipulation
- Service management permissions
- File system write access for logging

---

## 🚀 Installation Guide

### Automated Installation (Recommended)

```bash
# Clone the repository
git clone https://internal-git/anon-caller/system.git
cd system

# Execute setup script
chmod +x scripts/setup.sh
./scripts/setup.sh

# Activate virtual environment
source venv/bin/activate

# Verify installation
python src/main.py --help
```

### Manual Installation Steps

#### System Dependencies
```bash
sudo apt update
sudo apt install -y python3 python3-pip tor openvpn macchanger pjsua-dev
```

#### Python Environment Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

#### Service Configuration
```bash
sudo systemctl enable tor
sudo systemctl start tor
```

### Verification Commands

Check Tor status:
```bash
tor --version
curl --socks5-hostname localhost:9050 https://check.torproject.org/api/ip
```

Validate MAC changer:
```bash
macchanger --help
```

Test SIP library:
```bash
python -c "import pjsua; print('PJSIP loaded successfully')"
```

---

## ⚙️ Configuration

### Main Configuration File (`config.yaml`)

```yaml
sip:
  domain: "secure.anonymous.net"
  username: "anonymous_user"
  password: "encrypted_password_here"
  port: 5060
  transport: "udp"

tor:
  socks_port: 9050
  control_port: 9051
  restart_interval: 10
  circuit_timeout: 60

network:
  primary_interface: "eth0"
  backup_interface: "wlan0"
  mac_spoof_enabled: true

logging:
  level: "INFO"
  format: "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
  file_path: "/var/log/anonymous-caller/system.log"
  max_size_mb: 10
  retention_days: 30

security:
  encryption_level: "AES-256"
  key_rotation_minutes: 30
  certificate_validation: true
```

### Environment Variables

Create `.env` file for sensitive configurations:
```bash
export SIP_USERNAME="secure_user"
export SIP_PASSWORD="super_secret_password"
export TOR_CONTROL_PASSWORD="control_auth_key"
```

---

## ▶️ Usage Examples

### Basic Operation
```bash
# Interactive mode
python src/main.py

# Direct call initiation
python src/main.py --call "+1234567890"

# Background service mode
nohup python src/main.py > /dev/null 2>&1 &
```

### Advanced Parameters
```bash
# Custom configuration
python src/main.py --config custom-config.yaml --verbose

# Specific interface targeting
python src/main.py --interface wlan0 --interval 5

# Debug logging enabled
python src/main.py --debug --log-file debug.log
```

### Programmatic Integration
```python
from src.security.anonymity import enable_tor_vpn, auto_change_ip
from src.security.sip_caller import make_call
import asyncio

async def main():
    await enable_tor_vpn()
    asyncio.create_task(auto_change_ip(interval=15))
    make_call("+1987654321")

if __name__ == "__main__":
    asyncio.run(main())
```

---

## 🐳 Docker Deployment

### Build Image
```bash
docker build -t anonymous-caller:latest .
```

### Run Container
```bash
docker run -it --privileged \
  --network host \
  -v /var/log:/app/logs \
  anonymous-caller:latest
```

### Docker Compose (Development)
```yaml
version: '3.8'
services:
  anon-caller:
    build: .
    privileged: true
    network_mode: host
    volumes:
      - ./logs:/app/logs
    environment:
      - PYTHONUNBUFFERED=1
```

### Container Security Notes
- Privileged mode required for network interface manipulation
- Host networking recommended for optimal Tor performance
- Volume mapping for persistent logging
- Resource limits configurable via compose file

---

## ⚡ Performance Optimization

### Memory Management
- Garbage collection tuning for long-running processes
- Connection pooling for SIP sessions
- Efficient data structures for logging operations

### CPU Utilization
- Asynchronous I/O operations
- Non-blocking network calls
- Thread pool management for concurrent tasks

### Network Efficiency
- Connection reuse strategies
- Bandwidth optimization for Tor circuits
- Adaptive timing for IP rotation intervals

### Storage Optimization
- Log file compression and archiving
- Temporary file cleanup routines
- Cache invalidation mechanisms

---

## 📊 Logging & Monitoring

### Log Levels
- **DEBUG**: Detailed diagnostic information
- **INFO**: General operational messages
- **WARNING**: Potential issues requiring attention
- **ERROR**: Handled exceptions and failures
- **CRITICAL**: System-level emergencies

### Log Rotation Policy
- Maximum file size: 10MB
- Retention period: 30 days
- Compression enabled for archived logs
- Automatic cleanup of old entries

### Monitoring Endpoints
- Health check API endpoint
- Performance metrics collection
- Error rate tracking
- Resource utilization reporting

### Audit Trail Features
- Timestamp precision to microsecond level
- User action correlation
- System state snapshots
- Compliance reporting capabilities

---

## 🔐 Security Considerations

### Input Validation
- Strict parameter sanitization
- Regular expression pattern matching
- Length and format constraints
- Type checking enforcement

### Output Encoding
- Prevention of information disclosure
- Secure error message formatting
- Stack trace suppression in production

### Credential Management
- Encrypted storage for sensitive data
- Automatic credential rotation
- Secure memory handling
- Access control restrictions

### Runtime Protections
- Buffer overflow prevention
- Injection attack mitigation
- Race condition avoidance
- Privilege escalation safeguards

### Network Security
- Firewall rule compliance
- Port scanning detection resistance
- Traffic analysis countermeasures
- Protocol-level hardening

---

## 🧪 Testing Framework

### Unit Tests
Located in `/tests/` directory with coverage for:
- Configuration loading and validation
- Network service initialization
- SIP session establishment
- Error handling scenarios
- Logging functionality verification

### Integration Tests
- End-to-end call flow validation
- Multi-service coordination testing
- Performance benchmark assessments
- Security boundary verification

### Test Execution
```bash
# Run all tests
python -m pytest tests/

# Verbose output with coverage
python -m pytest tests/ -v --cov=src/

# Specific module testing
python -m pytest tests/test_sip_caller.py
```

### Continuous Testing
Integrated with GitHub Actions for:
- Pull request validation
- Branch protection rules
- Code quality gates
- Security scanning automation

---

## 🔄 CI/CD Integration

### GitHub Actions Pipeline
Automated workflow triggers on:
- Push events to main branch
- Pull request creation
- Scheduled weekly builds
- Manual dispatch options

### Pipeline Stages
1. **Code Checkout**: Repository synchronization
2. **Dependency Resolution**: Package installation verification
3. **Static Analysis**: Linting and style checking
4. **Unit Testing**: Automated test suite execution
5. **Security Scanning**: Vulnerability assessment
6. **Build Packaging**: Artifact creation
7. **Deployment Preparation**: Release candidate generation

### Quality Gates
- Minimum test coverage threshold (85%)
- Zero critical security vulnerabilities
- Successful linting compliance
- Performance regression checks

---

## 📁 Directory Structure

```
anonymous-caller/
├── src/                          # Core application source code
│   ├── __init__.py              # Package initialization
│   ├── config.py                # Configuration management
│   ├── logger.py                # Logging infrastructure
│   ├── security/                # Security-related modules
│   │   ├── anonymity.py         # Tor and VPN controls
│   │   ├── mac_spoof.py         # MAC address manipulation
│   │   └── sip_caller.py        # SIP communication handler
│   ├── cli.py                   # Command-line interface
│   └── main.py                  # Application entry point
├── scripts/                     # Automation and setup scripts
│   ├── setup.sh                 # Initial environment setup
│   └── install.sh               # Dependency installation
├── tests/                       # Automated testing suite
│   ├── __init__.py
│   ├── test_config.py
│   ├── test_logging.py
│   ├── test_anonymity.py
│   ├── test_mac_spoof.py
│   └── test_sip_caller.py
├── logs/                        # Application log files
├── docs/                        # Documentation resources
├── .github/                     # GitHub integration files
│   └── workflows/               # CI/CD pipeline definitions
├── Dockerfile                   # Container build specification
├── requirements.txt             # Python package dependencies
├── pyproject.toml               # Project metadata and build config
├── config.yaml                  # Default configuration file
├── .gitignore                   # Version control exclusions
└── README.md                    # This documentation file
```

---

## 🛠️ Troubleshooting

### Common Issues and Solutions

#### Tor Service Not Starting
```bash
# Check service status
sudo systemctl status tor

# Restart service
sudo systemctl restart tor

# View logs
journalctl -u tor -f
```

#### MAC Address Spoofing Failure
```bash
# Verify interface availability
ip link show eth0

# Check macchanger installation
which macchanger

# Manual interface reset
sudo ifconfig eth0 down
sudo macchanger -r eth0
sudo ifconfig eth0 up
```

#### SIP Registration Errors
Verify configuration parameters:
- Domain accessibility
- Credential validity
- Network connectivity
- Port availability

#### Permission Denied Errors
Ensure running with appropriate privileges:
```bash
sudo python src/main.py
```

Or add user to required groups:
```bash
sudo usermod -a -G netdev,dialout $USER
```

### Diagnostic Commands

Network diagnostics:
```bash
netstat -tuln | grep 5060
ss -tuln | grep tor
ps aux | grep tor
```

Service verification:
```bash
torify curl https://api.ipify.org
macchanger --show eth0
```

### Performance Monitoring
```bash
htop                      # System resource usage
iotop                     # Disk I/O monitoring
iftop                     # Network traffic analysis
```

---

## 📜 Version History

### v1.0.0 - Initial Release
- Core anonymous calling functionality
- Tor integration and IP rotation
- SIP communication implementation
- MAC address spoofing capability
- Basic configuration management
- Structured logging system
- Docker container support
- Automated installation scripts
- Unit testing framework
- CI/CD pipeline integration

### v1.1.0 - Performance Enhancement
- Asynchronous operation improvements
- Memory optimization techniques
- Enhanced error handling
- Extended logging capabilities
- Configuration validation enhancements
- Security hardening measures

### v1.2.0 - Enterprise Features
- Multi-interface support
- Advanced monitoring integration
- Compliance reporting features
- Scalability improvements
- Documentation expansion
- Bug fixes and stability improvements

---

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

**Disclaimer**: This software is provided for educational and research purposes only. The authors assume no liability for misuse or damage caused by improper usage. Users are responsible for ensuring compliance with all applicable laws and regulations.

---

*"In a world where digital footprints can compromise your identity, staying anonymous isn't just an option—it's a necessity."*

*Built for those who understand that true security comes from invisibility.*
