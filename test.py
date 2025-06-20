import webview
import keyboard
import threading
import json
import os
import pyautogui
import pystray
import sys
import uuid
import locale
import re
import time
import os
from pathlib import Path
from flask import Flask, render_template, request, jsonify, send_file, abort
from PIL import Image
from screeninfo import get_monitors
from plyer import notification
import zlib
import tempfile
import configparser