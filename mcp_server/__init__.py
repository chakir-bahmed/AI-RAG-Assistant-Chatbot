"""
SYNORA MCP Server
=================

A standalone, enterprise-grade Model Context Protocol (MCP) server that
provides comprehensive tools, resources, and prompts for AI-powered
development workflows.

Exposes pipeline orchestration, knowledge-base operations, code analysis,
file management, web retrieval, data processing, Git operations, and
system diagnostics through the standardized MCP interface.
"""

__version__ = "1.0.0"
__author__ = "SYNORA AI Team"

from .server import SYNORAMCPServer

__all__ = ["SYNORAMCPServer"]
