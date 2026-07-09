#!/usr/bin/env python3
"""
Email Checker for Jayden
- Reads IMAP settings from .env
- Checks for unread emails
- Saves new emails to drafts folder for translation
"""

import os
import imaplib
import email
from email.header import decode_header
from datetime import datetime
import sys

def load_env():
    """Load IMAP settings from .env file"""
    env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
    env_vars = {}
    if os.path.exists(env_path):
        with open(env_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    env_vars[key] = value.strip()
    return env_vars

def decode_email_header(header):
    """Decode email header to string"""
    if header is None:
        return ""
    decoded_parts = []
    for part, encoding in decode_header(header):
        if isinstance(part, bytes):
            decoded_parts.append(part.decode(encoding or 'utf-8', errors='replace'))
        else:
            decoded_parts.append(part)
    return ''.join(decoded_parts)

def get_email_body(msg):
    """Extract email body text"""
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            if content_type == 'text/plain':
                payload = part.get_payload(decode=True)
                charset = part.get_content_charset() or 'utf-8'
                body = payload.decode(charset, errors='replace')
                break
    else:
        payload = msg.get_payload(decode=True)
        charset = msg.get_content_charset() or 'utf-8'
        body = payload.decode(charset, errors='replace')
    return body

def check_emails():
    """Check emails and save to drafts folder"""
    env = load_env()
    
    host = env.get('EMAIL_IMAP_HOST')
    port = env.get('EMAIL_IMAP_PORT', '993')
    user = env.get('EMAIL_IMAP_USER')
    password = env.get('EMAIL_IMAP_PASSWORD')
    
    if not all([host, user, password]):
        print("Error: Missing IMAP configuration in .env")
        return
    
    try:
        # Connect to IMAP server
        mail = imaplib.IMAP4_SSL(host, int(port))
        mail.login(user, password)
        mail.select('INBOX')
        
        # Search for unread emails
        status, messages = mail.search(None, 'UNSEEN')
        
        if status != 'OK':
            print("No unread emails found")
            return
        
        email_ids = messages[0].split()
        print(f"Found {len(email_ids)} unread email(s)")
        
        drafts_dir = os.path.join(os.path.dirname(__file__), '..', '01_Action_Center', 'outputs', 'drafts')
        os.makedirs(drafts_dir, exist_ok=True)
        
        for eid in email_ids:
            status, msg_data = mail.fetch(eid, '(RFC822)')
            
            if status != 'OK':
                continue
                
            raw_email = msg_data[0][1]
            msg = email.message_from_bytes(raw_email)
            
            subject = decode_email_header(msg['Subject'])
            sender = decode_email_header(msg['From'])
            date = msg['Date']
            body = get_email_body(msg)
            
            # Save to drafts folder
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"email_{timestamp}.txt"
            filepath = os.path.join(drafts_dir, filename)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(f"Subject: {subject}\n")
                f.write(f"From: {sender}\n")
                f.write(f"Date: {date}\n")
                f.write(f"--- Email Body ---\n\n")
                f.write(body)
            
            print(f"Saved: {filename}")
        
        mail.logout()
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    check_emails()
