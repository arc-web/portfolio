# Domain Auditor Agent

A specialized domain intelligence agent that audits domain registration, hosting, DNS, SSL, and technical configuration.

## Capabilities

- **Domain Registration** - WHOIS lookup, registrar info, registration dates
- **Hosting Analysis** - IP geolocation, hosting provider, nameservers
- **DNS Records** - A, AAAA, MX, SPF, DKIM, CAA, TXT analysis
- **SSL/TLS** - Certificate validity, expiry, chain analysis, security grade
- **Tech Stack** - Web server, CMS, framework detection
- **Subdomains** - Enumeration, related domains, takeover risk

## Input Format

```json
{
  "domain": "example.com",
  "include_subdomains": true,
  "deep_scan": false,
  "registrant_email": "contact@example.com"
}
```

## Output Format

```json
{
  "domain": "example.com",
  "audit_timestamp": "2026-03-30T15:30:00Z",
  "registration": { ... },
  "hosting": { ... },
  "dns": { ... },
  "ssl": { ... },
  "tech_stack": { ... },
  "subdomains": { ... },
  "overall_score": 85,
  "findings": []
}
```

## Invocation

Via CLI: `python -m domain_auditor audit example.com --deep`
Via agent: Called by forensic audit orchestrator
