# Cloud-Based Credit Risk & Fraud Intelligence System

## Overview
This project implements a multi-layer financial risk intelligence system designed to simulate how modern banks assess fraud and credit risk before making operational decisions.

## Business Context
In real-world banking environments, fraud decisions are rarely binary. Institutions must combine transaction behavior, customer credit risk, and governance policies to decide whether to approve, block, or escalate a case for manual review.

This project models that layered decision-making process.

## System Architecture
The system is designed as three independent but connected engines:
1. Transaction Risk Engine – detects anomalous transaction behavior
2. Credit Risk Engine – evaluates customer-level default risk
3. Decision Engine – applies policy rules to classify outcomes

## Technical Approach
- Used Isolation Forest to detect anomalous transaction patterns
- Applied Logistic Regression for probability-based credit risk scoring
- Combined model outputs through a rule-based decision framework
- Classified outcomes into Fraud, Manual Review, or Not Fraud

## Cloud Architecture Alignment
The system is designed to align with cloud-native banking architectures:
- Amazon S3 for raw and processed data storage
- AWS EC2 or Lambda for independent risk engine execution
- AWS IAM for access control concepts
- Amazon CloudWatch for monitoring and auditability
- Analytics outputs designed for executive dashboards

## Governance & Explainability
- Supports human-in-the-loop review workflows
- Prioritizes decision transparency over black-box scoring
- Designed with regulatory and audit considerations in mind

## Skills Demonstrated
Python, Machine Learning, Credit Risk Modeling, Fraud Detection, Policy-Based Decision Systems, AWS Cloud Architecture, Financial Risk Analysis
