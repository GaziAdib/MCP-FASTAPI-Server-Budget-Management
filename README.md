# 🚀 FastMCP Custom Server From Scratch

<div align="center">

### *Build Production-Ready MCP Servers for LLM Tooling*

[![Python 3.14+](https://img.shields.io/badge/python-3.14+-blue.svg)](https://www.python.org/downloads/)
[![FastMCP](https://img.shields.io/badge/FastMCP-Latest-green.svg)](https://github.com/jlowin/fastmcp)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

*A practical, project-based course on building Model Context Protocol (MCP) servers with FastMCP—enabling Large Language Models to securely interact with tools, databases, and APIs.*

[📚 Documentation](#-overview) • [🎯 Features](#-core-features) • [🏗️ Architecture](#-architecture) • [🚦 Getting Started](#-getting-started)

</div>

---

## 📌 Overview

**FastMCP** is a Python framework that simplifies building servers compliant with the **Model Context Protocol (MCP)**—a modern standard for connecting LLMs like Claude and GPT with external tools, data sources, and web APIs.

This repository contains comprehensive learning materials that will take you from zero to building production-ready MCP servers. You'll learn to design, implement, and deploy both local (STDIO) and remote (HTTP/SSE) MCP servers with real database integrations and LLM-optimized tool design.

### Why This Matters

Traditional LLMs are isolated from real-world data. MCP bridges this gap by providing a standardized protocol for LLMs to safely interact with your databases, APIs, and tools—all while maintaining security and control.

---

## ✨ Core Features

<table>
<tr>
<td width="50%">

### 🎯 **Dual Server Architecture**
- **Local STDIO Servers** for development & debugging
- **Remote HTTP/SSE Servers** for production deployment
- Seamless transition from dev to prod

</td>
<td width="50%">

### 🔧 **Production-Ready Tools**
- Real database integrations (SQLite with raw SQL)
- Custom tool registration for LLMs
- CRUD operations with natural language

</td>
</tr>
<tr>
<td width="50%">

### ⚡ **Developer Experience**
- Minimal boilerplate code
- Pythonic and clean syntax
- FastAPI-friendly design
- Built-in transport support

</td>
<td width="50%">

### 🌐 **Scalable Patterns**
- One-to-one communication (STDIO)
- One-to-many communication (HTTP/SSE)
- Multi-user concurrent access support

</td>
</tr>
</table>

---

## 🏗️ Architecture

### System Overview

```
┌──────────────────────────────────────────────────────────────────┐
│                         LLM Client Layer                          │
│                    (Claude / GPT / Compatible)                    │
└───────────────────────────────┬──────────────────────────────────┘
                                │
                    Natural Language Request
                                │
┌───────────────────────────────▼──────────────────────────────────┐
│                       MCP Client Layer                            │
│                  (Inspector / SDK / Interface)                    │
└───────────────────────────────┬──────────────────────────────────┘
                                │
                    MCP Protocol Communication
                    (STDIO / HTTP / SSE)
                                │
┌───────────────────────────────▼──────────────────────────────────┐
│                      FastMCP Server Core                          │
│                   (Python Application Logic)                      │
├───────────────────────────────────────────────────────────────────┤
│  • Request Parser      • Tool Registry      • Response Builder   │
│  • Protocol Handler    • Security Layer     • Error Handler      │
└───────────────────────────────┬──────────────────────────────────┘
                                │
                       Tool Execution Layer
                                │
┌───────────────────────────────▼──────────────────────────────────┐
│                         Tools Layer                               │
│                   (Python Functions & Logic)                      │
├───────────────────────────────────────────────────────────────────┤
│  • Database Queries    • API Calls       • Data Processing       │
│  • Calculations        • File Operations • Custom Logic          │
└───────────────────────────────┬──────────────────────────────────┘
                                │
                        Data Access Layer
                                │
┌───────────────────────────────▼──────────────────────────────────┐
│                      Data Sources Layer                           │
│              (SQLite Database / External APIs)                    │
└───────────────────────────────────────────────────────────────────┘
```

### Request Flow

1. **LLM receives a user prompt** → Natural language instruction
2. **MCP Client processes** → Converts to MCP protocol
3. **FastMCP Server interprets** → Routes to appropriate tool
4. **Tool executes** → Performs database queries or API calls
5. **Data returns** → Structured response back through the chain
6. **LLM presents result** → Natural language output to user

---

## 🛠️ Tech Stack

### Core Technologies

| Category | Technology | Purpose |
|----------|-----------|---------|
| **Language** | Python 3.14+ | Server implementation |
| **Framework** | FastMCP | MCP server framework |
| **Database** | SQLite (Raw SQL) | Data persistence |
| **Protocols** | HTTP, SSE, STDIO | Transport layers |
| **Data Format** | JSON | Data serialization |
| **LLM Clients** | Claude, GPT-compatible | AI integration |

### Development Tools

- **MCP Inspector** - Server testing and debugging
- **Python Virtual Environment** - Dependency isolation
- **Git** - Version control

---

## 🎯 What You'll Learn

<details open>
<summary><b>🧠 Conceptual Knowledge</b></summary>

- What Model Context Protocol (MCP) is and its role in LLM ecosystems
- Why FastMCP is essential for building LLM tool servers
- Differences between Local (STDIO) and Remote (HTTP/SSE) architectures
- Development vs Production MCP server patterns
- One-to-one vs One-to-many communication paradigms

</details>

<details open>
<summary><b>💻 Practical Skills</b></summary>

- Building custom FastMCP servers from scratch
- Designing and registering LLM-friendly tools
- Implementing SQLite database connections with raw SQL
- Creating CRUD operations accessible via natural language
- Deploying both STDIO and HTTP/SSE transport modes
- Structuring MCP servers for real-world applications

</details>

<details open>
<summary><b>🏢 Production Patterns</b></summary>

- Architecting scalable MCP server infrastructure
- Implementing authentication and security layers
- Handling multiple concurrent LLM connections
- Connecting to external APIs and hosted databases
- Error handling and logging best practices

</details>

---

## 📋 Prerequisites

### Required Knowledge

| Area | Topics | Level |
|------|--------|-------|
| **Python** | Functions, Lists, Dictionaries, Comprehensions | Intermediate |
| **SQL** | SELECT, INSERT, UPDATE, DELETE queries | Basic |
| **APIs** | REST concepts, JSON data structures | Basic |

### System Requirements

- **Operating System**: Windows, macOS, or Linux
- **Python Version**: 3.14 or higher
- **Disk Space**: 500MB minimum
- **Internet**: Required for remote servers

> **Note**: No prior knowledge of MCP or FastMCP is required. We start from the fundamentals!

---

## 🚀 Course Project

By the end of this course, you'll build a **fully functional FastMCP server** with the following capabilities:

### Features Checklist

- ✅ Exposes multiple tools to LLMs
- ✅ Accepts natural language instructions
- ✅ Connects to SQLite database
- ✅ Performs complete CRUD operations
- ✅ Supports both STDIO and HTTP/SSE transports
- ✅ Implements production-ready patterns
- ✅ Includes error handling and logging
- ✅ Mimics real-world enterprise LLM tool servers

---

## 🚦 Getting Started

### Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/fastmcp-course.git

# Navigate to project directory
cd fastmcp-course

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run your first MCP server
python examples/hello_world_server.py
```

### Project Structure

```
fastmcp-course/
├── 📁 examples/           # Sample MCP servers
├── 📁 lessons/            # Course lessons and materials
├── 📁 projects/           # Hands-on projects
├── 📁 resources/          # Additional resources
├── 📄 requirements.txt    # Python dependencies
└── 📄 README.md          # This file
```

---

## 📚 Server Types Covered

### 🔹 Local MCP Server (STDIO)

**Perfect for Development & Learning**

| Feature | Details |
|---------|---------|
| **Deployment** | Runs entirely on local machine |
| **Communication** | Standard Input/Output streams |
| **Architecture** | One-to-one client-server |
| **Use Cases** | Learning, testing, debugging |
| **Speed** | Extremely fast, no network latency |
| **Internet** | Not required |
| **Debugging** | Easy to trace and debug |

### 🔹 Remote MCP Server (HTTP/SSE)

**Production-Ready Architecture**

| Feature | Details |
|---------|---------|
| **Deployment** | Cloud or remote server hosting |
| **Communication** | HTTP + Server-Sent Events |
| **Architecture** | One-to-many concurrent connections |
| **Use Cases** | Production applications |
| **Scalability** | Supports multiple users simultaneously |
| **Integration** | Hosted databases, external APIs |
| **Security** | Authentication, encryption required |

---

## 👥 Who This Is For

<table>
<tr>
<td align="center" width="20%">
<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/People/Technologist.png" width="60" />
<br><b>AI Developers</b>
</td>
<td align="center" width="20%">
<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Laptop.png" width="60" />
<br><b>Backend Developers</b>
</td>
<td align="center" width="20%">
<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Animals/Snake.png" width="60" />
<br><b>Python Engineers</b>
</td>
<td align="center" width="20%">
<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Gear.png" width="60" />
<br><b>Automation Engineers</b>
</td>
<td align="center" width="20%">
<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/People/Student.png" width="60" />
<br><b>Students</b>
</td>
</tr>
</table>

**If you want to build LLM-powered systems that interact with real databases and APIs, this course is for you.**

---

## ⚡ Why Choose FastMCP?

FastMCP stands out from other MCP implementations by providing:

| Advantage | Benefit |
|-----------|---------|
| **Minimal Boilerplate** | Focus on logic, not configuration |
| **Pythonic Syntax** | Clean, readable code that follows Python conventions |
| **FastAPI-Friendly** | Seamless integration with modern Python web frameworks |
| **Easy Tool Registration** | Register tools with simple decorators |
| **Built-in Transports** | STDIO and HTTP/SSE support out of the box |
| **LLM-Optimized** | Architecture designed specifically for LLM interactions |

---

## 📖 Course Modules

1. **Introduction to MCP** - Understanding the protocol
2. **FastMCP Basics** - Setup and first server
3. **Tool Design** - Creating LLM-friendly tools
4. **Database Integration** - SQLite with raw SQL
5. **STDIO Servers** - Local development patterns
6. **HTTP/SSE Servers** - Production deployment
7. **Real-World Project** - Building a complete system

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## ✍️ Author

<div align="center">

**Gazi Adib**

*AI & Backend Developer*

Specializing in FastMCP • Python • LLM Tooling

[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=social&logo=github)](https://github.com/gaziadib)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=social&logo=linkedin)](https://linkedin.com/in/gaziadib)
[![Twitter](https://img.shields.io/badge/Twitter-Follow-blue?style=social&logo=twitter)](https://twitter.com/gaziadib)

</div>

---

## 🌟 Acknowledgments

- The FastMCP team for creating an excellent framework
- The MCP community for their contributions and feedback
- All students and developers who provide valuable feedback

---

## 💬 Support

If you have questions or need help:

- 📫 Open an [Issue](https://github.com/yourusername/fastmcp-course/issues)
- 💬 Join our [Discord Community](https://discord.gg/your-invite)
- 📧 Email: your.email@example.com

---

<div align="center">

### ⭐ Final Note

*This course bridges the gap between LLMs and real-world systems using modern MCP standards.*

*Designed to be practical, clean, and production-oriented.*

**If you find this useful, consider giving the repo a ⭐**

---

**Happy Building! 🚀**

Made with ❤️ by developers, for developers

</div>