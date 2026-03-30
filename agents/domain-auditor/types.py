"""Type definitions for domain auditor."""
from dataclasses import dataclass, asdict
from typing import Optional, List, Dict, Any
from enum import Enum


class SSLGrade(str, Enum):
    """SSL certificate grade."""
    A_PLUS = "A+"
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    F = "F"


@dataclass
class RegistrationInfo:
    """Domain registration details."""
    registrar: str
    registered_date: Optional[str]
    expiry_date: Optional[str]
    registrant_name: Optional[str]
    registrant_email: Optional[str]
    nameservers: List[str]

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class HostingInfo:
    """Domain hosting details."""
    ip_address: str
    ip_version: int  # 4 or 6
    provider: str
    country: str
    asn: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class DNSRecords:
    """DNS record details."""
    a_records: List[str]
    aaaa_records: List[str]
    mx_records: List[Dict[str, str]]
    spf_record: Optional[str]
    dkim_records: List[str]
    caa_records: List[str]

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class SSLInfo:
    """SSL/TLS certificate details."""
    certificate_valid: bool
    issuer: str
    not_before: Optional[str]
    not_after: Optional[str]
    grade: SSLGrade

    def to_dict(self) -> Dict[str, Any]:
        data = asdict(self)
        data['grade'] = self.grade.value
        return data


@dataclass
class TechStackInfo:
    """Technology stack detection."""
    web_server: Optional[str]
    cms: Optional[str]
    frameworks: List[str]
    technologies: List[str]

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class SubdomainInfo:
    """Subdomain details."""
    name: str
    ip: Optional[str]
    provider: Optional[str]

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class DomainAuditReport:
    """Complete domain audit report."""
    domain: str
    audit_timestamp: str
    registration: RegistrationInfo
    hosting: HostingInfo
    dns: DNSRecords
    ssl: SSLInfo
    tech_stack: TechStackInfo
    subdomains: List[SubdomainInfo]
    overall_score: int
    findings: List[Dict[str, Any]]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "domain": self.domain,
            "audit_timestamp": self.audit_timestamp,
            "registration": self.registration.to_dict(),
            "hosting": self.hosting.to_dict(),
            "dns": self.dns.to_dict(),
            "ssl": self.ssl.to_dict(),
            "tech_stack": self.tech_stack.to_dict(),
            "subdomains": [s.to_dict() for s in self.subdomains],
            "overall_score": self.overall_score,
            "findings": self.findings
        }
