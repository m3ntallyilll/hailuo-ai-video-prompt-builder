from setuptools import setup, find_packages
import os
import shutil

# Create necessary directories
os.makedirs('hailuo_prompt_builder/static', exist_ok=True)
os.makedirs('hailuo_prompt_builder/templates', exist_ok=True)

# Create the main HTML file with FULL code
with open('hailuo_prompt_builder/templates/index.html', 'w') as f:
    f.write('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hailuo AI Video Prompt Builder - Pro Edition</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://js.stripe.com/v3/"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        primary: '#5D5CDE',
                        secondary: '#8C8CFF',
                        accent: '#FF5C8D',
                        success: '#4CAF50',
                        warning: '#FFC107',
                        danger: '#F44336',
                        dark: {
                            bg: '#121212',
                            card: '#1E1E1E',
                            border: '#333333',
                            accent: '#2C2C2C'
                        },
                        light: {
                            bg: '#F8F9FA',
                            card: '#FFFFFF',
                            border: '#E0E0E0',
                            accent: '#F1F3F5'
                        }
                    },
                    animation: {
                        'pulse-slow': 'pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite',
                        'bounce-slow': 'bounce 2s infinite',
                        'ping-slow': 'ping 2s cubic-bezier(0, 0, 0.2, 1) infinite',
                        'fade-in': 'fadeIn 0.5s ease-out',
                        'slide-in': 'slideIn 0.3s ease-out',
                        'slide-up': 'slideUp 0.4s ease-out',
                        'scale-in': 'scaleIn 0.3s ease-out',
                    },
                    keyframes: {
                        fadeIn: {
                            '0%': { opacity: '0' },
                            '100%': { opacity: '1' },
                        },
                        slideIn: {
                            '0%': { transform: 'translateX(-10px)', opacity: '0' },
                            '100%': { transform: 'translateX(0)', opacity: '1' },
                        },
                        slideUp: {
                            '0%': { transform: 'translateY(10px)', opacity: '0' },
                            '100%': { transform: 'translateY(0)', opacity: '1' },
                        },
                        scaleIn: {
                            '0%': { transform: 'scale(0.95)', opacity: '0' },
                            '100%': { transform: 'scale(1)', opacity: '1' },
                        },
                    },
                    boxShadow: {
                        'glow': '0 0 15px rgba(93, 92, 222, 0.5)',
                        'glow-sm': '0 0 5px rgba(93, 92, 222, 0.5)',
                    }
                }
            }
        }
    </script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/animate.css@4.1.1/animate.min.css">
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <style>
        /* Smooth scrolling and transitions */
        html {
            scroll-behavior: smooth;
        }
        
        * {
            transition: background-color 0.3s, border-color 0.3s, color 0.2s, box-shadow 0.3s, transform 0.2s;
        }
        
        /* Hide scrollbar by default */
        ::-webkit-scrollbar {
            width: 6px;
            height: 6px;
        }
        
        ::-webkit-scrollbar-track {
            background: transparent;
        }
        
        ::-webkit-scrollbar-thumb {
            background: rgba(93, 92, 222, 0.3);
            border-radius: 3px;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: rgba(93, 92, 222, 0.5);
        }
        
        .scrollbar-thin {
            scrollbar-width: thin;
            scrollbar-color: rgba(93, 92, 222, 0.3) transparent;
        }
        
        /* Glass morphism effect */
        .glassmorphism {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.18);
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        }
        
        .dark .glassmorphism {
            background: rgba(18, 18, 18, 0.7);
            border: 1px solid rgba(255, 255, 255, 0.08);
        }
        
        /* Custom slider styling */
        .realism-slider {
            -webkit-appearance: none;
            height: 8px;
            border-radius: 4px;
            background: linear-gradient(to right, #6366F1, #8B5CF6, #EC4899);
            outline: none;
        }
        
        .realism-slider::-webkit-slider-thumb {
            -webkit-appearance: none;
            appearance: none;
            width: 20px;
            height: 20px;
            border-radius: 50%;
            background: #FFFFFF;
            border: 2px solid #5D5CDE;
            cursor: pointer;
            box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        }
        
        .realism-slider::-moz-range-thumb {
            width: 20px;
            height: 20px;
            border-radius: 50%;
            background: #FFFFFF;
            border: 2px solid #5D5CDE;
            cursor: pointer;
            box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        }
        
        .dark .realism-slider::-webkit-slider-thumb {
            background: #1E1E1E;
            border-color: #8C8CFF;
        }
        
        .dark .realism-slider::-moz-range-thumb {
            background: #1E1E1E;
            border-color: #8C8CFF;
        }
        
        /* Camera control styling */
        .camera-btn {
            transition: all 0.2s ease;
        }
        
        .camera-btn:active {
            transform: scale(0.95);
        }
        
        .camera-btn.active {
            background-color: #5D5CDE;
            color: white;
            box-shadow: 0 0 8px rgba(93, 92, 222, 0.5);
        }
        
        .dark .camera-btn.active {
            background-color: #8C8CFF;
            box-shadow: 0 0 8px rgba(140, 140, 255, 0.5);
        }
        
        /* Dropdown styling */
        optgroup {
            font-weight: bold;
            color: #4B5563;
        }
        
        .dark optgroup {
            color: #9CA3AF;
        }

        /* Lyrics segment styling */
        .lyrics-segment {
            transition: all 0.2s ease;
        }
        
        .lyrics-segment:hover {
            border-color: #5D5CDE;
            transform: translateY(-2px);
        }
        
        .lyrics-segment.selected {
            border-color: #5D5CDE;
            background-color: rgba(93, 92, 222, 0.05);
            box-shadow: 0 4px 12px rgba(93, 92, 222, 0.15);
        }
        
        .dark .lyrics-segment.selected {
            background-color: rgba(93, 92, 222, 0.1);
            box-shadow: 0 4px 12px rgba(93, 92, 222, 0.25);
        }
        
        /* Highlight effect for recently generated */
        @keyframes highlight {
            0% { background-color: rgba(93, 92, 222, 0.3); }
            100% { background-color: transparent; }
        }
        
        @keyframes pulse-border {
            0% { border-color: rgba(93, 92, 222, 0.7); }
            50% { border-color: rgba(93, 92, 222, 0.3); }
            100% { border-color: rgba(93, 92, 222, 0.7); }
        }
        
        .highlight-animation {
            animation: highlight 2s ease;
        }
        
        .pulse-border-animation {
            animation: pulse-border 2s infinite;
        }
        
        /* Card hover effects */
        .card-hover {
            transition: all 0.3s ease;
        }
        
        .card-hover:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
        }
        
        .dark .card-hover:hover {
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3), 0 10px 10px -5px rgba(0, 0, 0, 0.2);
        }
        
        /* Input focus effects */
        .input-focus:focus {
            box-shadow: 0 0 0 3px rgba(93, 92, 222, 0.3);
        }
        
        /* Badge styles */
        .badge {
            @apply inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium;
        }
        
        /* Tooltip styles */
        .tooltip {
            position: relative;
            display: inline-block;
        }
        
        .tooltip .tooltip-text {
            visibility: hidden;
            width: 120px;
            background-color: #5D5CDE;
            color: white;
            text-align: center;
            border-radius: 6px;
            padding: 5px;
            position: absolute;
            z-index: 1;
            bottom: 125%;
            left: 50%;
            transform: translateX(-50%);
            opacity: 0;
            transition: opacity 0.3s;
        }
        
        .tooltip .tooltip-text::after {
            content: "";
            position: absolute;
            top: 100%;
            left: 50%;
            margin-left: -5px;
            border-width: 5px;
            border-style: solid;
            border-color: #5D5CDE transparent transparent transparent;
        }
        
        .tooltip:hover .tooltip-text {
            visibility: visible;
            opacity: 1;
        }
        
        /* Preview image effects */
        .preview-img {
            transition: all 0.5s ease;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
        }
        
        .dark .preview-img {
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.4), 0 4px 6px -2px rgba(0, 0, 0, 0.2);
        }
        
        /* Skeleton loading animation */
        @keyframes shimmer {
          0% {
            background-position: -200% 0;
          }
          100% {
            background-position: 200% 0;
          }
        }
        
        .skeleton {
          background: linear-gradient(90deg, 
             rgba(0, 0, 0, 0.06) 25%,
             rgba(0, 0, 0, 0.12) 37%,
             rgba(0, 0, 0, 0.06) 63%
          );
          background-size: 200% 100%;
          animation: shimmer 1.5s infinite;
        }
        
        .dark .skeleton {
          background: linear-gradient(90deg, 
             rgba(255, 255, 255, 0.06) 25%,
             rgba(255, 255, 255, 0.12) 37%,
             rgba(255, 255, 255, 0.06) 63%
          );
          background-size: 200% 100%;
        }
        
        /* AI Chat window styling */
        .chat-window {
            max-height: 300px;
            overflow-y: auto;
            scroll-behavior: smooth;
        }
        
        .chat-message {
            margin-bottom: 8px;
            padding: 8px 12px;
            border-radius: 8px;
            max-width: 80%;
            word-wrap: break-word;
        }
        
        .chat-message.user {
            background-color: #5D5CDE;
            color: white;
            align-self: flex-end;
            margin-left: auto;
            border-bottom-right-radius: 2px;
        }
        
        .chat-message.assistant {
            background-color: #F1F3F5;
            color: #333;
            align-self: flex-start;
            margin-right: auto;
            border-bottom-left-radius: 2px;
        }
        
        .dark .chat-message.assistant {
            background-color: #2C2C2C;
            color: #E0E0E0;
        }
        
        /* Toggle switch styling */
        .toggle-switch {
            position: relative;
            display: inline-block;
            width: 48px;
            height: 24px;
        }
        
        .toggle-switch input {
            opacity: 0;
            width: 0;
            height: 0;
        }
        
        .toggle-slider {
            position: absolute;
            cursor: pointer;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-color: #ccc;
            transition: .4s;
            border-radius: 24px;
        }
        
        .toggle-slider:before {
            position: absolute;
            content: "";
            height: 18px;
            width: 18px;
            left: 3px;
            bottom: 3px;
            background-color: white;
            transition: .4s;
            border-radius: 50%;
        }
        
        input:checked + .toggle-slider {
            background-color: #5D5CDE;
        }
        
        input:checked + .toggle-slider:before {
            transform: translateX(24px);
        }
        
        /* Tag styles */
        .tag {
            display: inline-flex;
            align-items: center;
            padding: 0.35rem 0.75rem;
            margin: 0.25rem;
            border-radius: 9999px;
            font-size: 0.75rem;
            font-weight: 500;
            background-color: #EEF2FF;
            color: #4F46E5;
            border: 1px solid #E0E7FF;
            transition: all 0.2s;
        }
        
        .tag:hover {
            background-color: #E0E7FF;
        }
        
        .dark .tag {
            background-color: #312E81;
            color: #C7D2FE;
            border-color: #4F46E5;
        }
        
        .dark .tag:hover {
            background-color: #4338CA;
        }
        
        .tag .remove {
            margin-left: 0.5rem;
            cursor: pointer;
        }
        
        /* Toast notification */
        .toast {
            position: fixed;
            bottom: 20px;
            right: 20px;
            padding: 10px 20px;
            border-radius: 8px;
            background-color: #5D5CDE;
            color: white;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            z-index: 1000;
            opacity: 0;
            transform: translateY(20px);
            transition: opacity 0.3s, transform 0.3s;
        }
        
        .toast.show {
            opacity: 1;
            transform: translateY(0);
        }
        
        /* Code mirror-like styles */
        .code-mirror {
            font-family: monospace;
            line-height: 1.5;
            border-radius: 6px;
            counter-reset: line;
        }
        
        .prompt-output {
            white-space: pre-wrap;
            word-break: break-word;
            font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            line-height: 1.5;
        }

        /* Tool execution display */
        .tool-execution {
            background-color: rgba(93, 92, 222, 0.1);
            border-left: 3px solid #5D5CDE;
            padding: 8px 12px;
            margin: 8px 0;
            font-size: 0.85em;
        }

        .dark .tool-execution {
            background-color: rgba(140, 140, 255, 0.1);
            border-left: 3px solid #8C8CFF;
        }

        .tool-execution-title {
            font-weight: 600;
            margin-bottom: 4px;
            color: #5D5CDE;
        }

        .dark .tool-execution-title {
            color: #8C8CFF;
        }
        
        /* Stripe payment form styling */
        .StripeElement {
            background-color: white;
            padding: 12px;
            border-radius: 6px;
            border: 1px solid #e0e0e0;
            box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);
            transition: all 0.2s ease;
            height: 40px;
        }

        .dark .StripeElement {
            background-color: #2c2c2c;
            border-color: #444;
            color: white;
        }

        .StripeElement--focus {
            box-shadow: 0 0 0 2px rgba(93, 92, 222, 0.4);
        }

        .StripeElement--invalid {
            border-color: #fa755a;
        }

        .StripeElement--webkit-autofill {
            background-color: #fefde5 !important;
        }
        
        /* Credit card brands */
        .card-brand {
            opacity: 0.5;
            transition: opacity 0.3s;
        }
        
        .card-brand.active {
            opacity: 1;
        }
        
        /* Pricing cards */
        .pricing-card {
            transition: all 0.3s ease;
            border: 2px solid transparent;
        }
        
        .pricing-card.selected {
            border-color: #5D5CDE;
            transform: scale(1.02);
            box-shadow: 0 10px 25px -5px rgba(93, 92, 222, 0.25), 0 8px 10px -6px rgba(93, 92, 222, 0.1);
        }
        
        .dark .pricing-card.selected {
            box-shadow: 0 10px 25px -5px rgba(140, 140, 255, 0.25), 0 8px 10px -6px rgba(140, 140, 255, 0.1);
        }
        
        /* Subscription badge */
        .subscription-badge {
            position: absolute;
            top: -8px;
            right: -8px;
            background: linear-gradient(45deg, #5D5CDE, #8C8CFF);
            color: white;
            border-radius: 9999px;
            padding: 0.25rem 0.5rem;
            font-size: 0.75rem;
            font-weight: 600;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            border: 2px solid white;
        }
        
        .dark .subscription-badge {
            border-color: #1e1e1e;
        }
    </style>
</head>
<body class="bg-light-bg dark:bg-dark-bg min-h-screen transition-colors duration-200">
    <div id="toast-container"></div>
    
    <div class="container max-w-6xl mx-auto px-4 py-6">
        <header class="mb-6 relative">
            <!-- Theme Toggle -->
            <div class="absolute right-0 top-0 flex items-center gap-2">
                <span class="text-sm text-gray-700 dark:text-gray-300">
                    <i class="far fa-sun"></i>
                </span>
                <label class="toggle-switch">
                    <input type="checkbox" id="theme-toggle">
                    <span class="toggle-slider"></span>
                </label>
                <span class="text-sm text-gray-700 dark:text-gray-300">
                    <i class="far fa-moon"></i>
                </span>
            </div>
            
            <!-- Account & Subscription Button -->
            <div class="absolute left-0 top-0 flex items-center gap-2">
                <button id="account-btn" class="px-3 py-1 text-sm border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-white rounded-md hover:bg-gray-100 dark:hover:bg-gray-600 flex items-center">
                    <i class="fas fa-user mr-1"></i> Account
                </button>
                <button id="subscription-btn" class="px-3 py-1 text-sm bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-700 hover:to-indigo-700 text-white rounded-md shadow-md hover:shadow-lg flex items-center">
                    <i class="fas fa-crown mr-1"></i> Upgrade
                </button>
            </div>
            
            <h1 class="text-3xl md:text-4xl font-bold text-gray-800 dark:text-white text-center mb-2 flex items-center justify-center">
                <span class="mr-3 text-primary">Hailuo</span>
                <span>AI Video Prompt Builder</span>
                <span class="ml-2 px-2 py-1 text-xs font-bold bg-primary text-white rounded">PRO</span>
            </h1>
            <p class="text-gray-600 dark:text-gray-300 text-center">Create optimized prompts for MiniMax Hailuo AI video models with advanced AI assistance</p>
            
            <!-- Mode Selector Tabs -->
            <div class="flex justify-center mt-4">
                <div class="inline-flex rounded-md shadow-md bg-light-card dark:bg-dark-card p-1" role="group">
                    <button type="button" id="tab-standard" class="px-4 py-2 text-sm font-medium rounded-md bg-primary text-white">
                        <i class="fas fa-magic mr-1"></i> Standard Prompt
                    </button>
                    <button type="button" id="tab-lyrics" class="px-4 py-2 text-sm font-medium rounded-md text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700">
                        <i class="fas fa-music mr-1"></i> Lyrics Visualizer
                    </button>
                    <button type="button" id="tab-comparisons" class="px-4 py-2 text-sm font-medium rounded-md text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700">
                        <i class="fas fa-code-compare mr-1"></i> Compare & Remix
                    </button>
                    <button type="button" id="tab-assistant" class="px-4 py-2 text-sm font-medium rounded-md text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700">
                        <i class="fas fa-robot mr-1"></i> AI Assistant
                    </button>
                </div>
            </div>
        </header>

        <!-- Main content area -->
        <div id="content-container" class="relative">
            <!-- Standard Prompt Builder Section -->
            <div id="standard-section" class="animate__animated animate__fadeIn">
                <!-- Prompt Library Drawer -->
                <div class="mb-4 bg-light-card dark:bg-dark-card rounded-lg shadow-md p-4 border border-light-border dark:border-dark-border card-hover">
                    <div class="flex justify-between items-center cursor-pointer" id="library-toggle">
                        <h3 class="font-semibold text-gray-700 dark:text-gray-200">
                            <i class="fas fa-bookmark mr-2 text-primary"></i> Prompt Library
                            <span class="text-xs text-gray-500 dark:text-gray-400 ml-2">(Click to expand)</span>
                        </h3>
                        <i class="fas fa-chevron-down text-gray-500 dark:text-gray-400 transform transition-transform" id="library-chevron"></i>
                    </div>
                    
                    <div id="library-content" class="hidden mt-4 animate__animated animate__fadeIn">
                        <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
                            <div class="col-span-1 md:col-span-2">
                                <div id="saved-prompts" class="grid grid-cols-1 sm:grid-cols-2 gap-3 max-h-72 overflow-y-auto scrollbar-thin p-1">
                                    <div class="text-center text-gray-500 dark:text-gray-400 py-8 col-span-1 sm:col-span-2">
                                        <i class="far fa-folder-open text-2xl mb-2"></i>
                                        <p>No saved prompts yet</p>
                                        <p class="text-xs mt-1">Create and save prompts to build your library</p>
                                    </div>
                                </div>
                            </div>
                            <div class="col-span-1 bg-light-accent dark:bg-dark-accent rounded-lg p-3">
                                <h4 class="font-medium text-gray-700 dark:text-gray-200 mb-2">Quick Actions</h4>
                                <div class="space-y-2">
                                    <button id="btn-save-prompt" class="w-full px-3 py-2 bg-primary hover:bg-secondary text-white rounded-md transition-colors duration-150 flex items-center justify-center" disabled>
                                        <i class="fas fa-save mr-2"></i> Save Current Prompt
                                    </button>
                                    <button id="btn-export-all" class="w-full px-3 py-2 bg-gray-600 hover:bg-gray-700 text-white rounded-md transition-colors duration-150 flex items-center justify-center" disabled>
                                        <i class="fas fa-file-export mr-2"></i> Export Library
                                    </button>
                                </div>
                                <div class="mt-4">
                                    <p class="text-xs text-gray-600 dark:text-gray-400 mb-1">Import from file or text:</p>
                                    <div class="flex space-x-2">
                                        <button id="btn-import-prompts" class="flex-1 px-2 py-1 text-xs bg-gray-200 hover:bg-gray-300 dark:bg-gray-700 dark:hover:bg-gray-600 text-gray-800 dark:text-gray-200 rounded">
                                            <i class="fas fa-file-import mr-1"></i> Import
                                        </button>
                                        <button id="btn-clear-library" class="flex-1 px-2 py-1 text-xs bg-red-100 hover:bg-red-200 dark:bg-red-900/30 dark:hover:bg-red-900/50 text-red-800 dark:text-red-200 rounded">
                                            <i class="fas fa-trash-alt mr-1"></i> Clear All
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <!-- Quick Preset Generator -->
                <div class="bg-light-card dark:bg-dark-card rounded-lg shadow-md p-4 border border-light-border dark:border-dark-border mb-4 card-hover">
                    <div class="flex flex-col md:flex-row gap-3 items-center">
                        <div class="flex-1 w-full">
                            <label for="preset-prompt" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">AI Configuration Assistant <span class="text-xs text-gray-500">(Describe what you want)</span></label>
                            <div class="relative">
                                <input type="text" id="preset-prompt" class="w-full px-3 py-2 text-base rounded-md border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-white input-focus" placeholder="E.g., 'anime fight scene' or 'dreamy music video in a forest'">
                                <button id="clear-preset-input" class="absolute right-2 top-1/2 transform -translate-y-1/2 text-gray-400 hover:text-gray-600 dark:hover:text-gray-300">
                                    <i class="fas fa-times-circle"></i>
                                </button>
                            </div>
                        </div>
                        <div class="md:mt-6 flex items-center space-x-2">
                            <button id="btn-generate-preset" class="px-4 py-2 bg-primary hover:bg-secondary text-white rounded-md transition-colors duration-150 flex items-center justify-center shadow-md hover:shadow-lg">
                                <i class="fas fa-wand-magic-sparkles mr-2"></i> Generate Settings
                            </button>
                            <button id="btn-research-subject" class="px-3 py-2 bg-indigo-500 hover:bg-indigo-600 text-white rounded-md transition-colors duration-150 flex items-center justify-center shadow-md hover:shadow-lg">
                                <i class="fas fa-search mr-1"></i> <span class="hidden sm:inline">Research</span>
                            </button>
                        </div>
                    </div>
                    <div id="preset-generating" class="hidden mt-2">
                        <div class="flex items-center space-x-2 text-sm text-primary dark:text-secondary">
                            <i class="fas fa-spinner fa-spin"></i>
                            <span>Configuring settings with AI...</span>
                        </div>
                    </div>
                    
                    <!-- Research Results Container -->
                    <div id="research-results" class="hidden mt-3 p-3 bg-blue-50 dark:bg-blue-900/10 rounded-md border border-blue-100 dark:border-blue-900/30">
                        <div class="flex justify-between items-start mb-2">
                            <h4 class="text-sm font-medium text-blue-800 dark:text-blue-300">Research Insights <span class="ml-1 px-1.5 py-0.5 text-xs bg-blue-100 dark:bg-blue-900/50 rounded-full">Powered by Groq Compound Beta</span></h4>
                            <button id="close-research" class="text-gray-500 hover:text-gray-700 dark:hover:text-gray-300">
                                <i class="fas fa-times"></i>
                            </button>
                        </div>
                        <div id="research-content" class="text-sm text-gray-700 dark:text-gray-300">
                            <div id="research-loading" class="flex items-center justify-center py-4">
                                <i class="fas fa-spinner fa-spin mr-2 text-primary"></i>
                                <span>Researching...</span>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Suggested Keywords -->
                    <div class="mt-3">
                        <p class="text-xs text-gray-600 dark:text-gray-400 mb-1">Try these popular presets:</p>
                        <div class="flex flex-wrap gap-2">
                            <button class="preset-keyword tag">cinematic car chase</button>
                            <button class="preset-keyword tag">anime character powers</button>
                            <button class="preset-keyword tag">fantasy landscape</button>
                            <button class="preset-keyword tag">cyberpunk city</button>
                            <button class="preset-keyword tag">space exploration</button>
                        </div>
                    </div>
                </div>

                <div class="grid grid-cols-1 lg:grid-cols-3 gap-4">
                    <div class="lg:col-span-2">
                        <!-- Main Prompt Builder -->
                        <div class="bg-light-card dark:bg-dark-card rounded-lg shadow-md p-5 border border-light-border dark:border-dark-border mb-4 card-hover">
                            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
                                <div>
                                    <label for="hailuo-model" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Hailuo Model</label>
                                    <select id="hailuo-model" class="w-full px-3 py-2 text-base rounded-md border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-white input-focus">
                                        <option value="standard">Standard (I2V-01) - Versatile, text or image+text</option>
                                        <option value="director" selected>Director (T2V-01) - Cinematic, camera controls</option>
                                        <option value="live">Live (2V-01-Live) - Animate artwork</option>
                                        <option value="subject">Subject (S2V-01) - Character consistency</option>
                                    </select>
                                </div>
                                <div>
                                    <label for="prompt-style" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Visual Style</label>
                                    <select id="prompt-style" class="w-full px-3 py-2 text-base rounded-md border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-white input-focus">
                                        <option value="cinematic">Cinematic/Hollywood</option>
                                        <option value="music-video" selected>Music Video Style</option>
                                        <option value="action">Action Sequence</option>
                                        <option value="commercial">Commercial/Advertisement</option>
                                        <option value="sci-fi">Sci-Fi</option>
                                        <option value="fantasy">Fantasy</option>
                                        <option value="anime">Anime/Manga</option>
                                        <option value="cartoon">Cartoon/Stylized</option>
                                    </select>
                                </div>
                            </div>
                            
                            <!-- Cartoon Style Dropdown -->
                            <div class="mb-4">
                                <label for="cartoon-style" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Animation/Cartoon Style</label>
                                <select id="cartoon-style" class="w-full px-3 py-2 text-base rounded-md border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-white input-focus">
                                    <option value="">No specific cartoon style</option>
                                    
                                    <optgroup label="Popular Animation Studios">
                                        <option value="disney">Disney Classic</option>
                                        <option value="pixar">Pixar 3D Animation</option>
                                        <option value="dreamworks">DreamWorks Animation</option>
                                        <option value="studio-ghibli">Studio Ghibli</option>
                                        <option value="cartoon-network">Cartoon Network</option>
                                        <option value="nickelodeon">Nickelodeon</option>
                                        <option value="south-park">South Park</option>
                                        <option value="simpsons">The Simpsons</option>
                                        <option value="family-guy">Family Guy</option>
                                    </optgroup>
                                    
                                    <optgroup label="Anime Styles">
                                        <option value="shounen-anime">Shōnen (Action-Oriented)</option>
                                        <option value="shoujo-anime">Shōjo (Romance/Drama)</option>
                                        <option value="mecha-anime">Mecha</option>
                                        <option value="chibi">Chibi (Super-Deformed)</option>
                                        <option value="anime-90s">90s Anime</option>
                                        <option value="anime-80s">80s Anime</option>
                                        <option value="modern-anime">Modern Anime (2010s+)</option>
                                        <option value="jojo-anime">JoJo's Bizarre Adventure</option>
                                        <option value="one-piece">One Piece</option>
                                        <option value="dragon-ball">Dragon Ball</option>
                                    </optgroup>
                                    
                                    <optgroup label="Classic Cartoon Eras">
                                        <option value="rubber-hose">Rubber Hose Animation (1920s)</option>
                                        <option value="golden-age">Golden Age Cartoons (1930s-1950s)</option>
                                        <option value="limited-animation">Limited Animation (1960s-1970s)</option>
                                        <option value="saturday-morning">Saturday Morning Cartoons (1980s)</option>
                                        <option value="renaissance-era">Animation Renaissance (1990s)</option>
                                    </optgroup>
                                    
                                    <optgroup label="Art Styles">
                                        <option value="cel-shaded">Cel-Shaded</option>
                                        <option value="watercolor">Watercolor Animation</option>
                                        <option value="stop-motion">Stop Motion Style</option>
                                        <option value="claymation">Claymation</option>
                                        <option value="cutout">Paper Cutout</option>
                                        <option value="rotoscope">Rotoscoped Animation</option>
                                        <option value="flash">Flash Animation</option>
                                        <option value="low-poly">Low-Poly 3D</option>
                                        <option value="pixel-art">Pixel Art</option>
                                        <option value="line-art">Minimalist Line Art</option>
                                    </optgroup>
                                    
                                    <optgroup label="International Styles">
                                        <option value="franco-belgian">Franco-Belgian Comics (Tintin)</option>
                                        <option value="soviet">Soviet Animation</option>
                                        <option value="bollywood">Bollywood Animation</option>
                                        <option value="chinese">Chinese Animation (Donghua)</option>
                                        <option value="korean">Korean Animation</option>
                                    </optgroup>
                                    
                                    <optgroup label="Web Animation">
                                        <option value="newgrounds">Newgrounds Flash Style</option>
                                        <option value="youtube">YouTube Animation</option>
                                        <option value="webtoon">Webtoon Style</option>
                                        <option value="animated-gif">Animated GIF Style</option>
                                    </optgroup>
                                </select>
                            </div>
                            
                            <!-- Realism Slider -->
                            <div class="mb-5">
                                <label for="realism-level" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Realism Level</label>
                                <div class="px-1">
                                    <input type="range" id="realism-level" class="realism-slider w-full" min="1" max="10" value="7">
                                    <div class="flex justify-between text-xs text-gray-600 dark:text-gray-400 mt-1 px-1">
                                        <span>Cartoon/Stylized</span>
                                        <span id="realism-value" class="font-medium text-primary dark:text-secondary">Moderately Realistic</span>
                                        <span>Photorealistic</span>
                                    </div>
                                </div>
                            </div>
                            
                            <!-- Enhanced Camera Controls -->
                            <div id="camera-controls-section" class="mb-5">
                                <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Camera Movement (Director model)</label>
                                
                                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-3">
                                    <!-- Camera Movement Type -->
                                    <div>
                                        <div class="grid grid-cols-3 gap-2">
                                            <button class="camera-btn px-2 py-2 text-sm rounded-md border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-white hover:bg-gray-100 dark:hover:bg-gray-600 tooltip" data-camera="tracking" title="Tracking Shot">
                                                <i class="fas fa-arrows-left-right-to-line"></i>
                                                <span class="ml-1 hidden sm:inline">Tracking</span>
                                                <span class="tooltip-text">Camera follows subject horizontally</span>
                                            </button>
                                            <button class="camera-btn px-2 py-2 text-sm rounded-md border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-white hover:bg-gray-100 dark:hover:bg-gray-600 tooltip" data-camera="dolly" title="Dolly Shot">
                                                <i class="fas fa-truck-fast"></i>
                                                <span class="ml-1 hidden sm:inline">Dolly</span>
                                                <span class="tooltip-text">Camera moves toward/away from subject</span>
                                            </button>
                                            <button class="camera-btn px-2 py-2 text-sm rounded-md border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-white hover:bg-gray-100 dark:hover:bg-gray-600 tooltip" data-camera="aerial" title="Aerial View">
                                                <i class="fas fa-drone"></i>
                                                <span class="ml-1 hidden sm:inline">Aerial</span>
                                                <span class="tooltip-text">Shot from above like a drone</span>
                                            </button>
                                        </div>
                                    </div>
                                    
                                    <!-- Camera Direction/Effect -->
                                    <div>
                                        <div class="grid grid-cols-3 gap-2">
                                            <button class="camera-btn px-2 py-2 text-sm rounded-md border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-white hover:bg-gray-100 dark:hover:bg-gray-600 active tooltip" data-camera="zoom" title="Zoom In/Out">
                                                <i class="fas fa-magnifying-glass"></i>
                                                <span class="ml-1 hidden sm:inline">Zoom</span>
                                                <span class="tooltip-text">Lens zooms in or out</span>
                                            </button>
                                            <button class="camera-btn px-2 py-2 text-sm rounded-md border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-white hover:bg-gray-100 dark:hover:bg-gray-600 tooltip" data-camera="pan" title="Pan Left/Right">
                                                <i class="fas fa-left-right"></i>
                                                <span class="ml-1 hidden sm:inline">Pan</span>
                                                <span class="tooltip-text">Camera pivots horizontally</span>
                                            </button>
                                            <button class="camera-btn px-2 py-2 text-sm rounded-md border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-white hover:bg-gray-100 dark:hover:bg-gray-600 tooltip" data-camera="shake" title="Camera Shake">
                                                <i class="fas fa-hurricane"></i>
                                                <span class="ml-1 hidden sm:inline">Shake</span>
                                                <span class="tooltip-text">Adds drama with shaky cam</span>
                                            </button>
                                        </div>
                                    </div>
                                </div>
                                
                                <!-- Additional Camera Options -->
                                <div class="grid grid-cols-2 md:grid-cols-4 gap-2">
                                    <label class="flex items-center space-x-2">
                                        <input type="checkbox" id="camera-push" class="rounded text-primary focus:ring-primary">
                                        <span class="text-gray-700 dark:text-gray-300">[Push in]</span>
                                    </label>
                                    <label class="flex items-center space-x-2">
                                        <input type="checkbox" id="camera-pullout" class="rounded text-primary focus:ring-primary">
                                        <span class="text-gray-700 dark:text-gray-300">[Pull out]</span>
                                    </label>
                                    <label class="flex items-center space-x-2">
                                        <input type="checkbox" id="camera-lowangle" class="rounded text-primary focus:ring-primary">
                                        <span class="text-gray-700 dark:text-gray-300">[Low angle]</span>
                                    </label>
                                    <label class="flex items-center space-x-2">
                                        <input type="checkbox" id="camera-overhead" class="rounded text-primary focus:ring-primary">
                                        <span class="text-gray-700 dark:text-gray-300">[Overhead]</span>
                                    </label>
                                    
                                    <!-- New Advanced Camera Controls -->
                                    <label class="flex items-center space-x-2">
                                        <input type="checkbox" id="camera-closeup" class="rounded text-primary focus:ring-primary">
                                        <span class="text-gray-700 dark:text-gray-300">[Close-up]</span>
                                    </label>
                                    <label class="flex items-center space-x-2">
                                        <input type="checkbox" id="camera-dutch" class="rounded text-primary focus:ring-primary">
                                        <span class="text-gray-700 dark:text-gray-300">[Dutch angle]</span>
                                    </label>
                                    <label class="flex items-center space-x-2">
                                        <input type="checkbox" id="camera-slowmo" class="rounded text-primary focus:ring-primary">
                                        <span class="text-gray-700 dark:text-gray-300">[Slow motion]</span>
                                    </label>
                                    <label class="flex items-center space-x-2">
                                        <input type="checkbox" id="camera-timelapse" class="rounded text-primary focus:ring-primary">
                                        <span class="text-gray-700 dark:text-gray-300">[Time lapse]</span>
                                    </label>
                                </div>
                            </div>
                            
                            <div class="mb-4">
                                <label for="prompt-subject" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Main Subject/Character</label>
                                <div class="relative">
                                    <input type="text" id="prompt-subject" class="w-full px-3 py-2 text-base rounded-md border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-white input-focus" placeholder="Character, person, or main element">
                                    <div id="subject-suggestions" class="hidden absolute z-10 mt-1 w-full bg-white dark:bg-gray-800 border border-gray-300 dark:border-gray-600 rounded-md shadow-lg max-h-60 overflow-auto">
                                        <!-- Suggestions will be added here dynamically -->
                                    </div>
                                </div>
                            </div>
                            
                            <div class="mb-4">
                                <label for="prompt-action" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Action/Scene Description</label>
                                <textarea id="prompt-action" rows="3" class="w-full px-3 py-2 text-base rounded-md border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-white input-focus" placeholder="What's happening in the scene?"></textarea>
                            </div>
                            
                            <div class="mb-4">
                                <label for="prompt-atmosphere" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Setting & Atmosphere</label>
                                <textarea id="prompt-atmosphere" rows="2" class="w-full px-3 py-2 text-base rounded-md border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-white input-focus" placeholder="Describe the environment, lighting, and mood"></textarea>
                            </div>
                            
                            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
                                <div>
                                    <label for="prompt-aspect" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Aspect Ratio</label>
                                    <select id="prompt-aspect" class="w-full px-3 py-2 text-base rounded-md border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-white input-focus">
                                        <option value="16:9">16:9 (Landscape - YouTube, etc.)</option>
                                        <option value="9:16">9:16 (Portrait - TikTok, Reels)</option>
                                        <option value="1:1">1:1 (Square - Instagram)</option>
                                        <option value="4:3">4:3 (Standard)</option>
                                        <option value="21:9">21:9 (Ultrawide Cinematic)</option>
                                        <option value="2.35:1">2.35:1 (Anamorphic Widescreen)</option>
                                    </select>
                                </div>
                                
                                <!-- Comprehensive Special Effects Dropdown -->
                                <div>
                                    <label for="special-effects" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Special Effects</label>
                                    <select id="special-effects" class="w-full px-3 py-2 text-base rounded-md border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-white input-focus">
                                        <option value="">No special effects</option>
                                        
                                        <optgroup label="Atmospheric Effects">
                                            <option value="fog">Fog/Mist</option>
                                            <option value="rain">Rain</option>
                                            <option value="snow">Snow</option>
                                            <option value="dust">Dust/Particles</option>
                                            <option value="smoke">Smoke</option>
                                            <option value="steam">Steam</option>
                                            <option value="clouds">Dramatic Clouds</option>
                                            <option value="sunbeams">Sunbeams/God Rays</option>
                                            <option value="sandstorm">Sandstorm</option>
                                            <option value="underwater">Underwater Caustics</option>
                                        </optgroup>
                                        
                                        <optgroup label="Lighting Effects">
                                            <option value="neon" selected>Neon/Colorful Lighting</option>
                                            <option value="spotlight">Spotlight</option>
                                            <option value="lens-flare">Lens Flare</option>
                                            <option value="volumetric">Volumetric Lighting</option>
                                            <option value="backlight">Dramatic Backlighting</option>
                                            <option value="strobe">Strobe Light</option>
                                            <option value="lightning">Lightning</option>
                                            <option value="fire">Fire/Flames</option>
                                            <option value="hdr">HDR Lighting</option>
                                            <option value="chiaroscuro">Chiaroscuro (Strong Contrast)</option>
                                        </optgroup>
                                        
                                        <optgroup label="Camera/Visual Effects">
                                            <option value="bokeh">Bokeh/Depth of Field</option>
                                            <option value="motion-blur">Motion Blur</option>
                                            <option value="slow-motion">Slow Motion</option>
                                            <option value="time-lapse">Time Lapse</option>
                                            <option value="dolly-zoom">Dolly Zoom (Vertigo Effect)</option>
                                            <option value="vignette">Vignette</option>
                                            <option value="film-grain">Film Grain</option>
                                            <option value="vhs">VHS Distortion</option>
                                            <option value="fisheye">Fisheye Lens</option>
                                            <option value="monochrome">Monochrome/Black & White</option>
                                        </optgroup>
                                        
                                        <optgroup label="Digital/Glitch Effects">
                                            <option value="glitch">Digital Glitch</option>
                                            <option value="pixelation">Pixelation</option>
                                            <option value="data-moshing">Datamoshing</option>
                                            <option value="rgb-split">RGB Split/Chromatic Aberration</option>
                                            <option value="scan-lines">Scan Lines</option>
                                            <option value="crt">CRT Monitor Effect</option>
                                            <option value="static">Static/Noise</option>
                                            <option value="hologram">Hologram</option>
                                            <option value="double-exposure">Double Exposure</option>
                                            <option value="broken-glass">Broken Glass/Shatter</option>
                                        </optgroup>
                                        
                                        <optgroup label="Energy/Magic Effects">
                                            <option value="particles">Floating Particles</option>
                                            <option value="energy-aura">Energy Aura</option>
                                            <option value="electric">Electricity/Lightning</option>
                                            <option value="magic-sparkles">Magic Sparkles</option>
                                            <option value="explosion">Explosion</option>
                                            <option value="laser-beam">Laser Beam</option>
                                            <option value="shockwave">Shockwave</option>
                                            <option value="portal">Portal Effect</option>
                                            <option value="force-field">Force Field</option>
                                            <option value="tron-lines">Tron-style Light Lines</option>
                                        </optgroup>
                                        
                                        <optgroup label="Art Style Effects">
                                            <option value="watercolor">Watercolor Effect</option>
                                            <option value="oil-painting">Oil Painting Filter</option>
                                            <option value="comic-book">Comic Book Style</option>
                                            <option value="cel-shading">Cel Shading</option>
                                            <option value="rotoscope">Rotoscope Effect</option>
                                            <option value="paper-cutout">Paper Cutout</option>
                                            <option value="pointillism">Pointillism</option>
                                            <option value="impressionist">Impressionist Painting Style</option>
                                            <option value="geometric">Geometric Abstract</option>
                                            <option value="8-bit">8-bit/Pixel Art Style</option>
                                        </optgroup>
                                        
                                        <optgroup label="Color Grading">
                                            <option value="sepia">Sepia Tone</option>
                                            <option value="technicolor">Technicolor</option>
                                            <option value="bleach-bypass">Bleach Bypass</option>
                                            <option value="cinematic-blue">Cinematic Blue</option>
                                            <option value="cinematic-orange">Cinematic Orange-Teal</option>
                                            <option value="cross-process">Cross Processing</option>
                                            <option value="neon-noir">Neon Noir</option>
                                            <option value="pastel">Pastel Colors</option>
                                            <option value="infrared">Infrared Look</option>
                                            <option value="day-for-night">Day For Night</option>
                                        </optgroup>
                                    </select>
                                </div>
                            </div>
                            
                            <div id="usage-notes" class="text-sm text-gray-600 dark:text-gray-400 mt-2 mb-4 p-3 bg-blue-50 dark:bg-blue-900/20 rounded-md">
                                <h3 class="font-semibold mb-1">Hailuo Model Tips:</h3>
                                <div id="model-tips-standard" class="hidden">
                                    <p>• Works with text-only prompts or text + image inputs</p>
                                    <p>• Maintains good object consistency across frames</p>
                                    <p>• Great for general purpose video generation</p>
                                </div>
                                <div id="model-tips-director" class="">
                                    <p>• Use camera commands like [Zoom in] or [Pan left] for precise control</p>
                                    <p>• Combine multiple camera actions in one clip</p>
                                    <p>• Best for cinematic, Hollywood-quality clips</p>
                                </div>
                                <div id="model-tips-live" class="hidden">
                                    <p>• Perfect for animating existing artwork</p>
                                    <p>• Preserves line art integrity while adding motion</p>
                                    <p>• Works with drawings, sketches, cartoons and comics</p>
                                </div>
                                <div id="model-tips-subject" class="hidden">
                                    <p>• Use a reference image of your subject for consistency</p>
                                    <p>• Maintains character appearance throughout the video</p>
                                    <p>• Great for putting specific characters in new scenarios</p>
                                </div>
                            </div>
                            
                            <!-- Pre-populated examples -->
                            <div class="mb-4">
                                <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Quick Start Templates</label>
                                <div class="grid grid-cols-1 sm:grid-cols-3 gap-2">
                                    <button id="template-music" class="text-left px-3 py-2 bg-blue-50 hover:bg-blue-100 dark:bg-blue-900/30 dark:hover:bg-blue-900/50 rounded-md transition-colors text-sm">
                                        <span class="font-medium block">Music Video</span>
                                        <span class="text-xs text-gray-500 dark:text-gray-400">Car chase, neon setting</span>
                                    </button>
                                    <button id="template-action" class="text-left px-3 py-2 bg-blue-50 hover:bg-blue-100 dark:bg-blue-900/30 dark:hover:bg-blue-900/50 rounded-md transition-colors text-sm">
                                        <span class="font-medium block">Action Sequence</span>
                                        <span class="text-xs text-gray-500 dark:text-gray-400">RPG combat with effects</span>
                                    </button>
                                    <button id="template-anime" class="text-left px-3 py-2 bg-blue-50 hover:bg-blue-100 dark:bg-blue-900/30 dark:hover:bg-blue-900/50 rounded-md transition-colors text-sm">
                                        <span class="font-medium block">Anime Style</span>
                                        <span class="text-xs text-gray-500 dark:text-gray-400">Character with stylized visuals</span>
                                    </button>
                                    <button id="template-scifi" class="text-left px-3 py-2 bg-blue-50 hover:bg-blue-100 dark:bg-blue-900/30 dark:hover:bg-blue-900/50 rounded-md transition-colors text-sm">
                                        <span class="font-medium block">Sci-Fi Explorer</span>
                                        <span class="text-xs text-gray-500 dark:text-gray-400">Futuristic exploration scene</span>
                                    </button>
                                    <button id="template-nature" class="text-left px-3 py-2 bg-blue-50 hover:bg-blue-100 dark:bg-blue-900/30 dark:hover:bg-blue-900/50 rounded-md transition-colors text-sm">
                                        <span class="font-medium block">Nature Documentary</span>
                                        <span class="text-xs text-gray-500 dark:text-gray-400">Sweeping landscape shots</span>
                                    </button>
                                    <button id="template-horror" class="text-left px-3 py-2 bg-blue-50 hover:bg-blue-100 dark:bg-blue-900/30 dark:hover:bg-blue-900/50 rounded-md transition-colors text-sm">
                                        <span class="font-medium block">Horror Suspense</span>
                                        <span class="text-xs text-gray-500 dark:text-gray-400">Tense, atmospheric scene</span>
                                    </button>
                                </div>
                            </div>
                            
                            <div class="flex flex-col sm:flex-row gap-3 mb-4">
                                <button id="btn-generate" class="px-4 py-2 bg-primary hover:bg-secondary text-white rounded-md transition-colors duration-150 flex items-center justify-center shadow-md hover:shadow-lg">
                                    <i class="fas fa-magic mr-2"></i> Create Prompt
                                </button>
                                <button id="btn-copy" class="px-4 py-2 bg-gray-600 hover:bg-gray-700 text-white rounded-md transition-colors duration-150 flex items-center justify-center shadow-md hover:shadow-lg">
                                    <i class="fas fa-copy mr-2"></i> Copy Prompt
                                </button>
                                <div class="flex-1 flex justify-end">
                                    <button id="btn-advanced-options" class="px-3 py-1 text-sm border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-white rounded-md hover:bg-gray-100 dark:hover:bg-gray-600 flex items-center">
                                        <i class="fas fa-sliders mr-1"></i> Advanced Options
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="lg:col-span-1">
                        <!-- Real-time Prompt Visualization -->
                        <div class="bg-light-card dark:bg-dark-card rounded-lg shadow-md p-5 border border-light-border dark:border-dark-border mb-4 card-hover">
                            <h2 class="text-xl font-semibold text-gray-800 dark:text-white mb-3">Prompt Visualization</h2>
                            
                            <div id="preview-container" class="mb-4 relative">
                                <div id="preview-loading" class="absolute inset-0 flex items-center justify-center bg-gray-100 dark:bg-gray-800 bg-opacity-80 dark:bg-opacity-80 rounded-md z-10 hidden">
                                    <div class="text-center">
                                        <i class="fas fa-circle-notch fa-spin text-3xl text-primary mb-2"></i>
                                        <p class="text-gray-700 dark:text-gray-300">Generating preview...</p>
                                    </div>
                                </div>
                                
                                <div id="preview-placeholder" class="h-48 md:h-64 flex items-center justify-center bg-gray-100 dark:bg-gray-800 rounded-md mb-2">
                                    <div class="text-center p-4">
                                        <i class="fas fa-image text-3xl text-gray-400 dark:text-gray-600 mb-2"></i>
                                        <p class="text-gray-500 dark:text-gray-400">Fill in the prompt details and click "Preview" to generate a concept image</p>
                                    </div>
                                </div>
                                
                                <img id="preview-image" class="w-full h-auto rounded-md preview-img hidden" src="" alt="AI-generated preview">
                                
                                <div class="flex justify-between mt-2">
                                    <button id="btn-preview" class="px-3 py-1 text-sm bg-primary hover:bg-secondary text-white rounded-md transition-colors duration-150 flex items-center shadow-sm">
                                        <i class="fas fa-eye mr-1"></i> Preview
                                    </button>
                                    <button id="btn-refresh-preview" class="px-3 py-1 text-sm bg-gray-200 hover:bg-gray-300 dark:bg-gray-700 dark:hover:bg-gray-600 text-gray-800 dark:text-white rounded-md transition-colors duration-150 flex items-center shadow-sm" disabled>
                                        <i class="fas fa-sync-alt mr-1"></i> Refresh
                                    </button>
                                </div>
                            </div>
                            
                            <!-- Prompt Quality Analyzer -->
                            <div class="mb-4">
                                <h3 class="text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Prompt Quality Analysis</h3>
                                <div id="quality-meter" class="w-full h-2 bg-gray-200 dark:bg-gray-700 rounded-full mb-2">
                                    <div id="quality-bar" class="h-2 bg-gray-400 dark:bg-gray-500 rounded-full" style="width: 0%"></div>
                                </div>
                                <div id="quality-feedback" class="text-xs text-gray-600 dark:text-gray-400">
                                    <p>Add more details to improve your prompt quality</p>
                                </div>
                            </div>
                            
                            <!-- Prompt Tags -->
                            <div class="mb-4">
                                <h3 class="text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Detected Themes</h3>
                                <div id="prompt-tags" class="flex flex-wrap">
                                    <div class="text-xs text-gray-500 dark:text-gray-400">
                                        Fill in prompt details to generate tags
                                    </div>
                                </div>
                            </div>
                            
                            <!-- Quick Fixes -->
                            <div>
                                <h3 class="text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">AI Suggestions</h3>
                                <div id="ai-suggestions" class="space-y-2">
                                    <div class="text-xs text-gray-500 dark:text-gray-400">
                                        Generate a prompt to see AI recommendations
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <!-- Generated Prompt -->
                <div id="result-container" class="bg-light-card dark:bg-dark-card rounded-lg shadow-md p-5 border border-light-border dark:border-dark-border mb-4 card-hover">
                    <div class="flex justify-between items-center mb-3">
                        <h2 class="text-xl font-semibold text-gray-800 dark:text-white">Optimized Hailuo AI Prompt</h2>
                        <div class="flex space-x-2">
                            <button id="btn-smart-variations" class="px-2 py-1 text-xs bg-indigo-100 hover:bg-indigo-200 dark:bg-indigo-900/30 dark:hover:bg-indigo-900/50 text-indigo-800 dark:text-indigo-200 rounded flex items-center">
                                <i class="fas fa-random mr-1"></i> Variations
                            </button>
                            <button id="btn-format-prompt" class="px-2 py-1 text-xs bg-green-100 hover:bg-green-200 dark:bg-green-900/30 dark:hover:bg-green-900/50 text-green-800 dark:text-green-200 rounded flex items-center">
                                <i class="fas fa-spell-check mr-1"></i> Format
                            </button>
                        </div>
                    </div>
                    
                    <div id="prompt-generating" class="hidden">
                        <div class="flex items-center justify-center py-6">
                            <div class="text-center">
                                <i class="fas fa-spinner fa-spin text-3xl text-primary mb-2"></i>
                                <p class="text-gray-700 dark:text-gray-300">Generating your prompt...</p>
                            </div>
                        </div>
                    </div>
                    
                    <textarea id="prompt-result" rows="8" class="w-full px-3 py-2 text-base rounded-md border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-white input-focus" placeholder="Your optimized Hailuo AI prompt will appear here..."></textarea>
                    
                    <div class="flex flex-col sm:flex-row gap-3 mt-4">
                        <button id="btn-amplify" class="px-4 py-2 bg-purple-600 hover:bg-purple-700 text-white rounded-md transition-colors duration-150 flex items-center justify-center shadow-md hover:shadow-lg">
                            <i class="fas fa-bolt mr-2"></i> Amplify Prompt
                        </button>
                        <button id="btn-translate" class="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-md transition-colors duration-150 flex items-center justify-center shadow-md hover:shadow-lg">
                            <i class="fas fa-language mr-2"></i> Translate
                        </button>
                        <button id="btn-save-to-library" class="px-4 py-2 bg-green-600 hover:bg-green-700 text-white rounded-md transition-colors duration-150 flex items-center justify-center shadow-md hover:shadow-lg">
                            <i class="fas fa-bookmark mr-2"></i> Save to Library
                        </button>
                    </div>
                    
                    <div id="amplify-generating" class="hidden mt-4">
                        <div class="flex items-center space-x-2 text-sm text-primary dark:text-secondary">
                            <i class="fas fa-spinner fa-spin"></i>
                            <span>Enhancing your prompt...</span>
                        </div>
                    </div>
                    
                    <div class="mt-3 text-sm text-gray-600 dark:text-gray-400">
                        <p>Use this prompt with MiniMax Hailuo AI video generation tools on platforms like getimg.ai</p>
                        <p class="mt-1">Remember: Hailuo AI generates short clips (a few seconds). For longer videos, create multiple clips and stitch them together.</p>
                    </div>
                </div>
            </div>
            
            <!-- Lyrics Visualizer Section -->
            <div id="lyrics-section" class="hidden animate__animated animate__fadeIn">
                <div class="bg-light-card dark:bg-dark-card rounded-lg shadow-md p-5 border border-light-border dark:border-dark-border mb-4 card-hover">
                    <h2 class="text-xl font-semibold text-gray-800 dark:text-white mb-3">Song Lyrics Visualizer</h2>
                    <p class="text-gray-600 dark:text-gray-300 mb-4">Break down song lyrics into video clips for AI video generation</p>
                    
                    <div class="mb-4">
                        <label for="song-title" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Song Title</label>
                        <input type="text" id="song-title" class="w-full px-3 py-2 text-base rounded-md border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-white input-focus" placeholder="Enter the song title">
                    </div>
                    
                    <div class="mb-4">
                        <label for="song-artist" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Artist</label>
                        <input type="text" id="song-artist" class="w-full px-3 py-2 text-base rounded-md border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-white input-focus" placeholder="Enter the artist name">
                    </div>
                    
                    <div class="mb-4">
                        <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Song Lyrics</label>
                        <div class="flex mb-2">
                            <button id="btn-auto-fetch-lyrics" class="px-3 py-1 text-xs bg-indigo-100 hover:bg-indigo-200 dark:bg-indigo-900/30 dark:hover:bg-indigo-900/50 text-indigo-800 dark:text-indigo-200 rounded">
                                <i class="fas fa-search mr-1"></i> Try to auto-fetch lyrics
                            </button>
                        </div>
                        <textarea id="song-lyrics" rows="10" class="w-full px-3 py-2 text-base rounded-md border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-white input-focus" placeholder="Paste song lyrics here..."></textarea>
                    </div>
                    
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
                        <div>
                            <label for="lyrics-clip-duration" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Clip Duration (seconds)</label>
                            <input type="number" id="lyrics-clip-duration" class="w-full px-3 py-2 text-base rounded-md border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-white input-focus" value="5" min="3" max="10" step="1">
                        </div>
                        
                        <div>
                            <label for="lyrics-visual-style" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Visual Style</label>
                            <select id="lyrics-visual-style" class="w-full px-3 py-2 text-base rounded-md border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-white input-focus">
                                <option value="music-video" selected>Music Video Style</option>
                                <option value="cinematic">Cinematic/Hollywood</option>
                                <option value="anime">Anime/Manga</option>
                                <option value="fantasy">Fantasy</option>
                                <option value="sci-fi">Sci-Fi</option>
                                <option value="noir">Noir/Moody</option>
                                <option value="abstract">Abstract/Artistic</option>
                                <option value="dreamy">Dreamy/Ethereal</option>
                            </select>
                        </div>
                    </div>
                    
                    <div class="mb-4">
                        <label for="lyrics-theme" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Visual Theme/Setting <span class="text-xs text-gray-500">(optional)</span></label>
                        <input type="text" id="lyrics-theme" class="w-full px-3 py-2 text-base rounded-md border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-white input-focus" placeholder="E.g., 'neon city', 'forest at sunset', 'underwater world'">
                    </div>
                    
                    <div class="mb-4">
                        <label for="lyrics-segmentation" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Segmentation Method</label>
                        <div class="grid grid-cols-1 sm:grid-cols-3 gap-2">
                            <button id="segment-by-lines" class="text-center px-3 py-2 bg-primary text-white rounded-md transition-colors text-sm">
                                By Lines
                            </button>
                            <button id="segment-by-verses" class="text-center px-3 py-2 bg-gray-200 dark:bg-gray-700 text-gray-800 dark:text-white rounded-md transition-colors text-sm">
                                By Verses
                            </button>
                            <button id="segment-by-stanzas" class="text-center px-3 py-2 bg-gray-200 dark:bg-gray-700 text-gray-800 dark:text-white rounded-md transition-colors text-sm">
                                By Stanzas
                            </button>
                        </div>
                    </div>
                    
                    <div class="flex flex-col sm:flex-row gap-3 mb-4">
                        <button id="btn-process-lyrics" class="px-4 py-2 bg-primary hover:bg-secondary text-white rounded-md transition-colors duration-150 flex items-center justify-center shadow-md hover:shadow-lg">
                            <i class="fas fa-cut mr-2"></i> Split Into Segments
                        </button>
                        <button id="btn-generate-all-prompts" class="px-4 py-2 bg-gray-600 hover:bg-gray-700 text-white rounded-md transition-colors duration-150 flex items-center justify-center shadow-md hover:shadow-lg" disabled>
                            <i class="fas fa-film mr-2"></i> Generate All Prompts
                        </button>
                        <button id="btn-export-segments" class="px-4 py-2 bg-green-600 hover:bg-green-700 text-white rounded-md transition-colors duration-150 flex items-center justify-center shadow-md hover:shadow-lg" disabled>
                            <i class="fas fa-file-export mr-2"></i> Export Segments
                        </button>
                    </div>
                    
                    <div id="lyrics-processing" class="hidden mb-4">
                        <div class="flex items-center space-x-2 text-sm text-primary dark:text-secondary">
                            <i class="fas fa-spinner fa-spin"></i>
                            <span>Processing lyrics...</span>
                        </div>
                    </div>
                </div>
                
                <!-- Lyrics Segments Container -->
                <div id="lyrics-segments-container" class="hidden mb-4">
                    <div class="bg-light-card dark:bg-dark-card rounded-lg shadow-md p-4 border border-light-border dark:border-dark-border mb-4 card-hover">
                        <div class="flex justify-between items-center mb-3">
                            <h3 class="text-lg font-semibold text-gray-800 dark:text-white">Lyrics Segments</h3>
                            <div class="text-sm text-gray-600 dark:text-gray-400">
                                <span id="segments-progress">0/0</span> segments generated
                            </div>
                        </div>
                        
                        <!-- Progress Bar for All Segments -->
                        <div class="w-full h-2 bg-gray-200 dark:bg-gray-700 rounded-full mb-4">
                            <div id="segments-progress-bar" class="h-2 bg-primary rounded-full" style="width: 0%"></div>
                        </div>
                        
                        <div id="lyrics-segments" class="space-y-3 max-h-96 overflow-y-auto scrollbar-thin">
                            <!-- Segments will be added here dynamically -->
                        </div>
                    </div>
                    
                    <!-- Selected Segment Prompt -->
                    <div id="segment-prompt-container" class="hidden bg-light-card dark:bg-dark-card rounded-lg shadow-md p-5 border border-light-border dark:border-dark-border card-hover">
                        <div class="flex justify-between items-center mb-3">
                            <h3 class="text-lg font-semibold text-gray-800 dark:text-white">Segment Prompt</h3>
                            <span id="segment-number" class="px-2 py-1 bg-primary text-white text-sm rounded-md">Segment #1</span>
                        </div>
                        
                        <div id="segment-lyric-display" class="mb-4 p-3 bg-blue-50 dark:bg-blue-900/20 rounded-md">
                            <p class="text-gray-700 dark:text-gray-300 italic">Lyrics will appear here</p>
                        </div>
                        
                        <div class="mb-4">
                            <label for="segment-prompt" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">AI Video Prompt</label>
                            <textarea id="segment-prompt" rows="6" class="w-full px-3 py-2 text-base rounded-md border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-white input-focus" placeholder="Generated prompt will appear here..."></textarea>
                        </div>
                        
                        <div id="segment-generating" class="hidden mb-4">
                            <div class="flex items-center space-x-2 text-sm text-primary dark:text-secondary">
                                <i class="fas fa-spinner fa-spin"></i>
                                <span>Generating segment prompt...</span>
                            </div>
                        </div>
                        
                        <div class="flex flex-col sm:flex-row gap-3">
                            <button id="btn-generate-segment" class="px-4 py-2 bg-primary hover:bg-secondary text-white rounded-md transition-colors duration-150 flex items-center justify-center shadow-md hover:shadow-lg">
                                <i class="fas fa-magic mr-2"></i> Generate Prompt
                            </button>
                            <button id="btn-copy-segment" class="px-4 py-2 bg-gray-600 hover:bg-gray-700 text-white rounded-md transition-colors duration-150 flex items-center justify-center shadow-md hover:shadow-lg">
                                <i class="fas fa-copy mr-2"></i> Copy Prompt
                            </button>
                            <button id="btn-update-segment" class="px-4 py-2 bg-green-600 hover:bg-green-700 text-white rounded-md transition-colors duration-150 flex items-center justify-center shadow-md hover:shadow-lg">
                                <i class="fas fa-save mr-2"></i> Save Changes
                            </button>
                            <button id="btn-preview-segment" class="px-4 py-2 bg-purple-600 hover:bg-purple-700 text-white rounded-md transition-colors duration-150 flex items-center justify-center shadow-md hover:shadow-lg">
                                <i class="fas fa-eye mr-2"></i> Preview
                            </button>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Comparisons & Remix Section -->
            <div id="comparisons-section" class="hidden animate__animated animate__fadeIn">
                <div class="bg-light-card dark:bg-dark-card rounded-lg shadow-md p-5 border border-light-border dark:border-dark-border mb-4 card-hover">
                    <h2 class="text-xl font-semibold text-gray-800 dark:text-white mb-3">Compare & Remix Prompts</h2>
                    <p class="text-gray-600 dark:text-gray-300 mb-4">Generate multiple variations of prompts and compare them side by side</p>
                    
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
                        <div>
                            <label for="remix-base-prompt" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Base Prompt</label>
                            <textarea id="remix-base-prompt" rows="4" class="w-full px-3 py-2 text-base rounded-md border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-white input-focus" placeholder="Enter or paste a base prompt for remixing"></textarea>
                        </div>
                        
                        <div>
                            <label for="remix-instruction" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Remix Instructions</label>
                            <textarea id="remix-instruction" rows="4" class="w-full px-3 py-2 text-base rounded-md border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-white input-focus" placeholder="E.g., 'Make it more cyberpunk', 'Change the setting to underwater', 'Add more dynamic action'"></textarea>
                        </div>
                    </div>
                    
                    <div class="flex flex-col sm:flex-row gap-3 mb-4">
                        <button id="btn-generate-variants" class="px-4 py-2 bg-primary hover:bg-secondary text-white rounded-md transition-colors duration-150 flex items-center justify-center shadow-md hover:shadow-lg">
                            <i class="fas fa-code-branch mr-2"></i> Generate Variants
                        </button>
                        <button id="btn-compare-variants" class="px-4 py-2 bg-indigo-600 hover:bg-indigo-700 text-white rounded-md transition-colors duration-150 flex items-center justify-center shadow-md hover:shadow-lg">
                            <i class="fas fa-columns mr-2"></i> Side-by-Side Compare
                        </button>
                        <button id="btn-merge-prompts" class="px-4 py-2 bg-green-600 hover:bg-green-700 text-white rounded-md transition-colors duration-150 flex items-center justify-center shadow-md hover:shadow-lg">
                            <i class="fas fa-object-group mr-2"></i> Merge Prompts
                        </button>
                    </div>
                    
                    <div id="variants-generating" class="hidden mb-4">
                        <div class="flex items-center space-x-2 text-sm text-primary dark:text-secondary">
                            <i class="fas fa-spinner fa-spin"></i>
                            <span>Generating variants...</span>
                        </div>
                    </div>
                </div>
                
                <!-- Variants Display -->
                <div id="variants-container" class="hidden mb-4">
                    <div class="bg-light-card dark:bg-dark-card rounded-lg shadow-md p-4 border border-light-border dark:border-dark-border card-hover">
                        <h3 class="text-lg font-semibold text-gray-800 dark:text-white mb-3">Prompt Variants</h3>
                        <div id="variants-grid" class="grid grid-cols-1 md:grid-cols-2 gap-4">
                            <!-- Variants will be added here dynamically -->
                        </div>
                    </div>
                </div>
                
                <!-- Side-by-Side Comparison -->
                <div id="comparison-container" class="hidden mb-4">
                    <div class="bg-light-card dark:bg-dark-card rounded-lg shadow-md p-4 border border-light-border dark:border-dark-border card-hover">
                        <h3 class="text-lg font-semibold text-gray-800 dark:text-white mb-3">Side-by-Side Comparison</h3>
                        
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                            <div>
                                <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Prompt A</label>
                                <select id="comparison-a" class="w-full px-3 py-2 text-base rounded-md border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-white input-focus">
                                    <option value="">Select a prompt</option>
                                </select>
                                <div id="comparison-a-content" class="mt-2 p-3 bg-blue-50 dark:bg-blue-900/20 rounded-md text-sm text-gray-700 dark:text-gray-300 max-h-64 overflow-y-auto scrollbar-thin">
                                    Select a prompt to compare
                                </div>
                            </div>
                            
                            <div>
                                <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Prompt B</label>
                                <select id="comparison-b" class="w-full px-3 py-2 text-base rounded-md border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-white input-focus">
                                    <option value="">Select a prompt</option>
                                </select>
                                <div id="comparison-b-content" class="mt-2 p-3 bg-blue-50 dark:bg-blue-900/20 rounded-md text-sm text-gray-700 dark:text-gray-300 max-h-64 overflow-y-auto scrollbar-thin">
                                    Select a prompt to compare
                                </div>
                            </div>
                        </div>
                        
                        <div class="mt-4">
                            <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Difference Analysis</label>
                            <div id="comparison-diff" class="p-3 bg-gray-50 dark:bg-gray-800/50 rounded-md text-sm text-gray-700 dark:text-gray-300 max-h-48 overflow-y-auto scrollbar-thin">
                                Select two prompts to see differences
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- AI Assistant Section -->
            <div id="assistant-section" class="hidden animate__animated animate__fadeIn">
                <div class="grid grid-cols-1 lg:grid-cols-3 gap-4">
                    <div class="lg:col-span-2">
                        <div class="bg-light-card dark:bg-dark-card rounded-lg shadow-md p-5 border border-light-border dark:border-dark-border mb-4 card-hover">
                            <div class="flex justify-between items-center mb-2">
                                <h2 class="text-xl font-semibold text-gray-800 dark:text-white">AI Prompt Assistant</h2>
                                <span id="assistant-engine-badge" class="px-2 py-1 text-xs bg-indigo-100 dark:bg-indigo-900/30 text-indigo-800 dark:text-indigo-200 rounded-full">
                                    Powered by <span id="current-assistant-model">Groq Compound Beta</span>
                                </span>
                            </div>
                            <p class="text-gray-600 dark:text-gray-300 mb-3">Get help with prompt creation from our AI assistant</p>
                            
                            <!-- Agentic Capabilities Banner -->
                            <div id="agentic-capabilities-banner" class="mb-4 p-3 bg-gradient-to-r from-blue-50 to-indigo-50 dark:from-blue-900/20 dark:to-indigo-900/20 rounded-md border border-blue-100 dark:border-blue-900/30">
                                <div class="flex items-start">
                                    <div class="flex-shrink-0 pt-0.5">
                                        <i class="fas fa-robot text-blue-500 dark:text-blue-400"></i>
                                    </div>
                                    <div class="ml-3">
                                        <h3 class="text-sm font-medium text-blue-800 dark:text-blue-300">Enhanced AI with Groq Compound Beta</h3>
                                        <div class="mt-1 text-xs text-blue-700 dark:text-blue-400">
                                            <p>This assistant can now:</p>
                                            <ul class="list-disc list-inside mt-1 space-y-1">
                                                <li id="search-capability">Search the web for real-time information</li>
                                                <li id="code-capability">Use code to analyze data and solve problems</li>
                                            </ul>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            
                            <!-- Chat Window -->
                            <div id="chat-window" class="bg-gray-50 dark:bg-gray-800 rounded-md p-3 mb-4 h-80 overflow-y-auto chat-window flex flex-col scrollbar-thin">
                                <div class="chat-message assistant">
                                    <p>Hi! I'm your Hailuo AI Prompt Assistant. How can I help you create amazing video prompts today?</p>
                                </div>
                            </div>
                            
                            <!-- Chat Input -->
                            <div class="flex">
                                <input type="text" id="chat-input" class="flex-1 px-3 py-2 text-base rounded-l-md border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-white input-focus" placeholder="Ask me anything about prompt creation...">
                                <button id="btn-send-message" class="px-4 py-2 bg-primary hover:bg-secondary text-white rounded-r-md transition-colors duration-150 flex items-center justify-center">
                                    <i class="fas fa-paper-plane"></i>
                                </button>
                            </div>
                            
                            <!-- Suggested Questions -->
                            <div class="mt-4">
                                <h3 class="text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Suggested Questions:</h3>
                                <div class="flex flex-wrap gap-2">
                                    <button class="suggested-question px-3 py-1 text-xs bg-blue-50 hover:bg-blue-100 dark:bg-blue-900/30 dark:hover:bg-blue-900/50 text-blue-800 dark:text-blue-200 rounded transition-colors">How do I make my prompts more cinematic?</button>
                                    <button class="suggested-question px-3 py-1 text-xs bg-blue-50 hover:bg-blue-100 dark:bg-blue-900/30 dark:hover:bg-blue-900/50 text-blue-800 dark:text-blue-200 rounded transition-colors">What camera movements work best?</button>
                                    <button class="suggested-question px-3 py-1 text-xs bg-blue-50 hover:bg-blue-100 dark:bg-blue-900/30 dark:hover:bg-blue-900/50 text-blue-800 dark:text-blue-200 rounded transition-colors">How can I create better anime-style videos?</button>
                                    <button class="suggested-question px-3 py-1 text-xs bg-blue-50 hover:bg-blue-100 dark:bg-blue-900/30 dark:hover:bg-blue-900/50 text-blue-800 dark:text-blue-200 rounded transition-colors">What aspect ratio is best for TikTok?</button>
                                </div>
                                
                                <div id="agentic-questions" class="mt-3">
                                    <h3 class="text-sm font-medium text-indigo-700 dark:text-indigo-300 mb-2">Try with Agentic AI:</h3>
                                    <div class="flex flex-wrap gap-2">
                                        <button class="suggested-question px-3 py-1 text-xs bg-indigo-50 hover:bg-indigo-100 dark:bg-indigo-900/30 dark:hover:bg-indigo-900/50 text-indigo-800 dark:text-indigo-200 rounded transition-colors">What are the latest trends in AI video generation?</button>
                                        <button class="suggested-question px-3 py-1 text-xs bg-indigo-50 hover:bg-indigo-100 dark:bg-indigo-900/30 dark:hover:bg-indigo-900/50 text-indigo-800 dark:text-indigo-200 rounded transition-colors">Find visual references for a cyberpunk cityscape</button>
                                        <button class="suggested-question px-3 py-1 text-xs bg-indigo-50 hover:bg-indigo-100 dark:bg-indigo-900/30 dark:hover:bg-indigo-900/50 text-indigo-800 dark:text-indigo-200 rounded transition-colors">Compare Hailuo AI with other video generation models</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="lg:col-span-1">
                        <!-- Tips and Reference -->
                        <div class="bg-light-card dark:bg-dark-card rounded-lg shadow-md p-5 border border-light-border dark:border-dark-border mb-4 card-hover">
                            <h3 class="text-lg font-semibold text-gray-800 dark:text-white mb-3">Hailuo AI Quick Reference</h3>
                            
                            <div class="space-y-4">
                                <div>
                                    <h4 class="font-medium text-gray-700 dark:text-gray-200 mb-1">Model Capabilities</h4>
                                    <ul class="list-disc list-inside text-sm text-gray-600 dark:text-gray-400 space-y-1">
                                        <li>Standard (I2V-01): Text or image+text inputs</li>
                                        <li>Director (T2V-01): Camera controls like [Zoom in]</li>
                                        <li>Live (2V-01-Live): Animate static artwork</li>
                                        <li>Subject (S2V-01): Character consistency</li>
                                    </ul>
                                </div>
                                
                                <div>
                                    <h4 class="font-medium text-gray-700 dark:text-gray-200 mb-1">Camera Commands</h4>
                                    <div class="text-sm text-gray-600 dark:text-gray-400">
                                        Add these in [brackets] for Director model:
                                        <div class="grid grid-cols-2 gap-x-2 gap-y-1 mt-1">
                                            <div>[Zoom in]</div>
                                            <div>[Zoom out]</div>
                                            <div>[Pan left]</div>
                                            <div>[Pan right]</div>
                                            <div>[Push in]</div>
                                            <div>[Pull out]</div>
                                            <div>[Low angle]</div>
                                            <div>[Overhead]</div>
                                            <div>[Tracking shot]</div>
                                            <div>[Dolly shot]</div>
                                        </div>
                                    </div>
                                </div>
                                
                                <div>
                                    <h4 class="font-medium text-gray-700 dark:text-gray-200 mb-1">Advanced Tips</h4>
                                    <ul class="list-disc list-inside text-sm text-gray-600 dark:text-gray-400 space-y-1">
                                        <li>Use specific visual details rather than generic descriptions</li>
                                        <li>Mention lighting, atmosphere, and setting details</li>
                                        <li>Balance between 5-10 second clips for best results</li>
                                        <li>Add "--aspect 16:9" at the end to set ratio</li>
                                    </ul>
                                </div>
                                
                                <!-- Groq Compound Beta Section -->
                                <div id="compound-beta-info" class="pt-1 pb-1">
                                    <div class="flex justify-between items-center">
                                        <h4 class="font-medium text-gray-700 dark:text-gray-200 mb-1">Groq Compound Beta</h4>
                                        <span class="text-xs px-1.5 py-0.5 bg-green-100 dark:bg-green-900/20 text-green-800 dark:text-green-200 rounded-full">Active</span>
                                    </div>
                                    <ul class="list-disc list-inside text-sm text-gray-600 dark:text-gray-400 space-y-1">
                                        <li>Accesses real-time information through web search</li>
                                        <li>Executes Python code for advanced capabilities</li>
                                        <li>Provides up-to-date reference images & examples</li>
                                        <li>Optimizes prompts with current AI video trends</li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Subscription Modal -->
        <div id="subscription-modal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 hidden animate__animated animate__fadeIn">
            <div class="bg-white dark:bg-dark-card rounded-lg shadow-lg max-w-4xl w-full mx-4 max-h-[90vh] overflow-y-auto">
                <div class="p-5">
                    <div class="flex justify-between items-center mb-4">
                        <h3 class="text-xl font-semibold text-gray-800 dark:text-white">Choose Your Plan</h3>
                        <button id="close-subscription-modal" class="text-gray-500 hover:text-gray-700 dark:hover:text-gray-300">
                            <i class="fas fa-times text-xl"></i>
                        </button>
                    </div>
                    
                    <!-- Progress Steps -->
                    <div class="relative mb-8">
                        <div class="flex justify-between">
                            <div class="w-1/3 text-center">
                                <div id="step-1-indicator" class="w-8 h-8 mx-auto bg-primary text-white rounded-full flex items-center justify-center">
                                    <i class="fas fa-tag"></i>
                                </div>
                                <div class="mt-2 text-sm font-medium text-gray-800 dark:text-gray-200">Choose Plan</div>
                            </div>
                            <div class="w-1/3 text-center">
                                <div id="step-2-indicator" class="w-8 h-8 mx-auto bg-gray-300 dark:bg-gray-700 text-gray-500 dark:text-gray-400 rounded-full flex items-center justify-center">
                                    <i class="fas fa-credit-card"></i>
                                </div>
                                <div class="mt-2 text-sm font-medium text-gray-500 dark:text-gray-400">Payment</div>
                            </div>
                            <div class="w-1/3 text-center">
                                <div id="step-3-indicator" class="w-8 h-8 mx-auto bg-gray-300 dark:bg-gray-700 text-gray-500 dark:text-gray-400 rounded-full flex items-center justify-center">
                                    <i class="fas fa-check"></i>
                                </div>
                                <div class="mt-2 text-sm font-medium text-gray-500 dark:text-gray-400">Confirmation</div>
                            </div>
                        </div>
                        <div class="absolute top-4 left-0 right-0 mx-auto" style="height: 2px; width: 70%;">
                            <div class="h-full bg-gray-300 dark:bg-gray-700"></div>
                            <div id="progress-bar" class="h-full bg-primary transition-all duration-500" style="width: 0%; margin-top: -2px;"></div>
                        </div>
                    </div>
                    
                    <!-- Step 1: Plan Selection -->
                    <div id="plan-selection-step" class="animate__animated animate__fadeIn">
                        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
                            <!-- Free Plan -->
                            <div id="free-plan" class="pricing-card bg-white dark:bg-gray-800 rounded-lg shadow-md overflow-hidden relative">
                                <div class="p-6">
                                    <h4 class="text-xl font-bold text-gray-900 dark:text-white mb-1">Free</h4>
                                    <p class="text-gray-600 dark:text-gray-400 mb-4 h-12">Basic prompt creation for occasional users</p>
                                    <div class="text-3xl font-bold text-gray-900 dark:text-white mb-4">$0<span class="text-sm font-normal text-gray-600 dark:text-gray-400">/month</span></div>
                                    <ul class="text-sm text-gray-600 dark:text-gray-400 mb-6 space-y-2">
                                        <li class="flex items-start">
                                            <i class="fas fa-check text-green-500 mt-1 mr-2"></i>
                                            <span>Basic prompt generation</span>
                                        </li>
                                        <li class="flex items-start">
                                            <i class="fas fa-check text-green-500 mt-1 mr-2"></i>
                                            <span>Standard AI Assistant</span>
                                        </li>
                                        <li class="flex items-start">
                                            <i class="fas fa-check text-green-500 mt-1 mr-2"></i>
                                            <span>Save up to 5 prompts</span>
                                        </li>
                                        <li class="flex items-start opacity-50">
                                            <i class="fas fa-times text-red-500 mt-1 mr-2"></i>
                                            <span>No Agentic AI tools</span>
                                        </li>
                                        <li class="flex items-start opacity-50">
                                            <i class="fas fa-times text-red-500 mt-1 mr-2"></i>
                                            <span>Limited prompt variations</span>
                                        </li>
                                    </ul>
                                    <button class="select-plan-btn w-full py-2 px-4 bg-gray-200 hover:bg-gray-300 dark:bg-gray-700 dark:hover:bg-gray-600 text-gray-800 dark:text-white rounded-md transition-colors" data-plan="free">
                                        Current Plan
                                    </button>
                                </div>
                            </div>
                            
                            <!-- Pro Plan -->
                            <div id="pro-plan" class="pricing-card bg-white dark:bg-gray-800 rounded-lg shadow-md overflow-hidden relative transform scale-105 border-2 border-primary">
                                <div class="subscription-badge">Popular</div>
                                <div class="absolute top-0 left-0 right-0 h-1 bg-gradient-to-r from-blue-500 via-purple-500 to-pink-500"></div>
                                <div class="p-6">
                                    <h4 class="text-xl font-bold text-gray-900 dark:text-white mb-1">Pro</h4>
                                    <p class="text-gray-600 dark:text-gray-400 mb-4 h-12">Enhanced features for regular content creators</p>
                                    <div class="text-3xl font-bold text-gray-900 dark:text-white mb-4">$19<span class="text-sm font-normal text-gray-600 dark:text-gray-400">/month</span></div>
                                    <ul class="text-sm text-gray-600 dark:text-gray-400 mb-6 space-y-2">
                                        <li class="flex items-start">
                                            <i class="fas fa-check text-green-500 mt-1 mr-2"></i>
                                            <span>Everything in Free</span>
                                        </li>
                                        <li class="flex items-start">
                                            <i class="fas fa-check text-green-500 mt-1 mr-2"></i>
                                            <span>Unlimited prompt saving</span>
                                        </li>
                                        <li class="flex items-start">
                                            <i class="fas fa-check text-green-500 mt-1 mr-2"></i>
                                            <span>Web research with Groq</span>
                                        </li>
                                        <li class="flex items-start">
                                            <i class="fas fa-check text-green-500 mt-1 mr-2"></i>
                                            <span>Advanced prompt variations</span>
                                        </li>
                                        <li class="flex items-start">
                                            <i class="fas fa-check text-green-500 mt-1 mr-2"></i>
                                            <span>Bulk prompt generation</span>
                                        </li>
                                    </ul>
                                    <button class="select-plan-btn w-full py-2 px-4 bg-primary hover:bg-secondary text-white rounded-md transition-colors" data-plan="pro">
                                        Select Plan
                                    </button>
                                </div>
                            </div>
                            
                            <!-- Enterprise Plan -->
                            <div id="enterprise-plan" class="pricing-card bg-white dark:bg-gray-800 rounded-lg shadow-md overflow-hidden relative">
                                <div class="p-6">
                                    <h4 class="text-xl font-bold text-gray-900 dark:text-white mb-1">Studio</h4>
                                    <p class="text-gray-600 dark:text-gray-400 mb-4 h-12">For professional video production teams</p>
                                    <div class="text-3xl font-bold text-gray-900 dark:text-white mb-4">$49<span class="text-sm font-normal text-gray-600 dark:text-gray-400">/month</span></div>
                                    <ul class="text-sm text-gray-600 dark:text-gray-400 mb-6 space-y-2">
                                        <li class="flex items-start">
                                            <i class="fas fa-check text-green-500 mt-1 mr-2"></i>
                                            <span>Everything in Pro</span>
                                        </li>
                                        <li class="flex items-start">
                                            <i class="fas fa-check text-green-500 mt-1 mr-2"></i>
                                            <span>Team collaboration</span>
                                        </li>
                                        <li class="flex items-start">
                                            <i class="fas fa-check text-green-500 mt-1 mr-2"></i>
                                            <span>Custom branding</span>
                                        </li>
                                        <li class="flex items-start">
                                            <i class="fas fa-check text-green-500 mt-1 mr-2"></i>
                                            <span>API access</span>
                                        </li>
                                        <li class="flex items-start">
                                            <i class="fas fa-check text-green-500 mt-1 mr-2"></i>
                                            <span>Priority support</span>
                                        </li>
                                    </ul>
                                    <button class="select-plan-btn w-full py-2 px-4 bg-gray-800 hover:bg-gray-900 dark:bg-gray-600 dark:hover:bg-gray-500 text-white rounded-md transition-colors" data-plan="enterprise">
                                        Select Plan
                                    </button>
                                </div>
                            </div>
                        </div>
                        
                        <div class="text-center text-gray-600 dark:text-gray-400 text-sm mb-6">
                            All plans include a 7-day free trial. Cancel anytime.
                        </div>
                    </div>
                    
                    <!-- Step 2: Payment Information -->
                    <div id="payment-step" class="hidden animate__animated animate__fadeIn">
                        <div class="max-w-2xl mx-auto">
                            <div class="bg-blue-50 dark:bg-blue-900/20 p-4 rounded-lg mb-6">
                                <div class="flex items-start">
                                    <div class="flex-shrink-0">
                                        <i class="fas fa-info-circle text-blue-500 mt-1"></i>
                                    </div>
                                    <div class="ml-3">
                                        <h4 class="text-sm font-medium text-blue-800 dark:text-blue-300">Starting your <span id="selected-plan-name">Pro</span> plan</h4>
                                        <div class="mt-1 text-sm text-blue-700 dark:text-blue-400">
                                            <p>Your card will not be charged until your 7-day free trial ends.</p>
                                            <p class="mt-1">After that, you'll be billed <span id="selected-plan-price">$19</span> monthly.</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            
                            <div class="mb-6">
                                <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Email Address</label>
                                <input type="email" id="payment-email" class="w-full px-3 py-2 text-base rounded-md border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-white input-focus" placeholder="your.email@example.com">
                            </div>
                            
                            <div class="mb-6">
                                <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Card Information</label>
                                <div class="bg-white dark:bg-gray-800 rounded-md border border-gray-300 dark:border-gray-600 p-4">
                                    <div class="mb-4">
                                        <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Card Number</label>
                                        <div id="card-number-element" class="StripeElement p-3 border border-gray-300 dark:border-gray-600 rounded-md">
                                            <!-- Stripe Element will be inserted here -->
                                            <div class="text-gray-500 dark:text-gray-400 text-sm">4242 4242 4242 4242 (Demo card)</div>
                                        </div>
                                    </div>
                                    
                                    <div class="grid grid-cols-2 gap-4">
                                        <div>
                                            <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Expiration Date</label>
                                            <div id="card-expiry-element" class="StripeElement p-3 border border-gray-300 dark:border-gray-600 rounded-md">
                                                <!-- Stripe Element will be inserted here -->
                                                <div class="text-gray-500 dark:text-gray-400 text-sm">12/30</div>
                                            </div>
                                        </div>
                                        <div>
                                            <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">CVC</label>
                                            <div id="card-cvc-element" class="StripeElement p-3 border border-gray-300 dark:border-gray-600 rounded-md">
                                                <!-- Stripe Element will be inserted here -->
                                                <div class="text-gray-500 dark:text-gray-400 text-sm">123</div>
                                            </div>
                                        </div>
                                    </div>
                                    
                                    <div class="mt-4 flex justify-between items-center">
                                        <div class="text-sm text-gray-600 dark:text-gray-400">
                                            <i class="fas fa-lock mr-1"></i> Secured by Stripe
                                        </div>
                                        <div class="flex space-x-2">
                                            <img src="https://cdn.jsdelivr.net/gh/atakan/payment-icons@master/min/visa.svg" alt="Visa" class="h-6 card-brand active">
                                            <img src="https://cdn.jsdelivr.net/gh/atakan/payment-icons@master/min/mastercard.svg" alt="Mastercard" class="h-6 card-brand active">
                                            <img src="https://cdn.jsdelivr.net/gh/atakan/payment-icons@master/min/amex.svg" alt="Amex" class="h-6 card-brand active">
                                            <img src="https://cdn.jsdelivr.net/gh/atakan/payment-icons@master/min/discover.svg" alt="Discover" class="h-6 card-brand">
                                        </div>
                                    </div>
                                </div>
                                <div id="card-errors" class="mt-2 text-sm text-red-600 dark:text-red-400"></div>
                            </div>
                            
                            <div class="mb-6">
                                <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Billing Address</label>
                                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                                    <div>
                                        <input type="text" id="billing-name" class="w-full px-3 py-2 text-base rounded-md border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-white input-focus" placeholder="Full Name">
                                    </div>
                                    <div>
                                        <input type="text" id="billing-country" class="w-full px-3 py-2 text-base rounded-md border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-white input-focus" placeholder="Country">
                                    </div>
                                </div>
                            </div>
                            
                            <div class="flex items-start mb-6">
                                <div class="flex items-center h-5">
                                    <input id="terms-agreement" type="checkbox" class="w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-blue-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-blue-600 dark:ring-offset-gray-800">
                                </div>
                                <label for="terms-agreement" class="ml-2 text-sm text-gray-600 dark:text-gray-400">
                                    I agree to the <a href="#" class="text-primary hover:underline">Terms of Service</a> and <a href="#" class="text-primary hover:underline">Privacy Policy</a>
                                </label>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Step 3: Confirmation -->
                    <div id="confirmation-step" class="hidden animate__animated animate__fadeIn">
                        <div class="max-w-lg mx-auto text-center">
                            <div class="mb-6">
                                <div class="mx-auto w-16 h-16 bg-green-100 dark:bg-green-900/30 rounded-full flex items-center justify-center">
                                    <i class="fas fa-check text-2xl text-green-500"></i>
                                </div>
                            </div>
                            
                            <h4 class="text-xl font-semibold text-gray-800 dark:text-white mb-2">Subscription Activated!</h4>
                            <p class="text-gray-600 dark:text-gray-400 mb-6">Your <span id="confirmed-plan-name">Pro</span> plan is now active with a 7-day free trial.</p>
                            
                            <div class="bg-light-accent dark:bg-dark-accent rounded-lg p-4 mb-6">
                                <h5 class="font-medium text-gray-800 dark:text-white mb-2">What's included in your plan:</h5>
                                <ul id="confirmed-plan-features" class="text-sm text-gray-600 dark:text-gray-400 space-y-1">
                                    <li>• Unlimited prompt saving</li>
                                    <li>• Web research with Groq</li>
                                    <li>• Advanced prompt variations</li>
                                    <li>• Bulk prompt generation</li>
                                </ul>
                            </div>
                            
                            <p class="text-sm text-gray-600 dark:text-gray-400 mb-8">
                                A confirmation email has been sent to <span id="confirmed-email" class="font-medium">your.email@example.com</span>
                            </p>
                            
                            <button id="start-using-btn" class="px-6 py-3 bg-primary hover:bg-secondary text-white rounded-md transition-colors duration-150 flex items-center justify-center shadow-md hover:shadow-lg mx-auto">
                                <i class="fas fa-rocket mr-2"></i> Start Using Pro Features
                            </button>
                        </div>
                    </div>
                    
                    <!-- Navigation Buttons -->
                    <div class="flex justify-between pt-6 border-t border-gray-200 dark:border-gray-700">
                        <button id="back-btn" class="px-4 py-2 bg-gray-200 hover:bg-gray-300 dark:bg-gray-700 dark:hover:bg-gray-600 text-gray-800 dark:text-white rounded-md hidden">
                            <i class="fas fa-arrow-left mr-2"></i> Back
                        </button>
                        <div class="flex-1"></div>
                        <button id="next-btn" class="px-4 py-2 bg-primary hover:bg-secondary text-white rounded-md">
                            Continue <i class="fas fa-arrow-right ml-2"></i>
                        </button>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Account Modal -->
        <div id="account-modal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 hidden animate__animated animate__fadeIn">
            <div class="bg-white dark:bg-dark-card rounded-lg shadow-lg max-w-md w-full mx-4 max-h-[90vh] overflow-y-auto">
                <div class="p-5">
                    <div class="flex justify-between items-center mb-4">
                        <h3 class="text-xl font-semibold text-gray-800 dark:text-white">Your Account</h3>
                        <button id="close-account-modal" class="text-gray-500 hover:text-gray-700 dark:hover:text-gray-300">
                            <i class="fas fa-times text-xl"></i>
                        </button>
                    </div>
                    
                    <div class="mb-6">
                        <div class="flex items-center space-x-4">
                            <div class="w-16 h-16 bg-primary text-white rounded-full flex items-center justify-center text-2xl">
                                <i class="fas fa-user"></i>
                            </div>
                            <div>
                                <h4 class="text-lg font-medium text-gray-800 dark:text-white">Guest User</h4>
                                <p class="text-sm text-gray-600 dark:text-gray-400">Free Plan</p>
                            </div>
                        </div>
                    </div>
                    
                    <div class="mb-6">
                        <h4 class="text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Current Subscription</h4>
                        <div class="bg-light-accent dark:bg-dark-accent rounded-lg p-4">
                            <div class="flex justify-between items-center">
                                <div>
                                    <p class="font-medium text-gray-800 dark:text-white">Free Plan</p>
                                    <p class="text-sm text-gray-600 dark:text-gray-400">Basic features, limited to 5 saved prompts</p>
                                </div>
                                <button id="upgrade-from-account" class="px-3 py-1 text-xs bg-primary hover:bg-secondary text-white rounded-md transition-colors">
                                    Upgrade
                                </button>
                            </div>
                        </div>
                    </div>
                    
                    <div class="mb-6">
                        <h4 class="text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Usage Statistics</h4>
                        <div class="grid grid-cols-2 gap-4">
                            <div class="bg-white dark:bg-gray-800 rounded-lg p-4 border border-light-border dark:border-dark-border">
                                <p class="text-xs text-gray-600 dark:text-gray-400">Prompts Created</p>
                                <p class="text-2xl font-bold text-gray-800 dark:text-white">12</p>
                            </div>
                            <div class="bg-white dark:bg-gray-800 rounded-lg p-4 border border-light-border dark:border-dark-border">
                                <p class="text-xs text-gray-600 dark:text-gray-400">Saved Prompts</p>
                                <p class="text-2xl font-bold text-gray-800 dark:text-white">3<span class="text-xs font-normal text-gray-500 dark:text-gray-400">/5</span></p>
                            </div>
                        </div>
                    </div>
                    
                    <div class="border-t border-gray-200 dark:border-gray-700 pt-4">
                        <button id="sign-out-btn" class="w-full py-2 px-4 bg-gray-200 hover:bg-gray-300 dark:bg-gray-700 dark:hover:bg-gray-600 text-gray-800 dark:text-white rounded-md transition-colors">
                            <i class="fas fa-sign-out-alt mr-2"></i> Sign Out
                        </button>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Advanced Options Modal -->
        <div id="advanced-options-modal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 hidden animate__animated animate__fadeIn">
            <div class="bg-white dark:bg-dark-card rounded-lg shadow-lg max-w-2xl w-full mx-4 max-h-[90vh] overflow-y-auto">
                <div class="p-5">
                    <div class="flex justify-between items-center mb-4">
                        <h3 class="text-xl font-semibold text-gray-800 dark:text-white">Advanced Options</h3>
                        <button id="close-advanced-options" class="text-gray-500 hover:text-gray-700 dark:hover:text-gray-300">
                            <i class="fas fa-times text-xl"></i>
                        </button>
                    </div>
                    
                    <div class="space-y-5">
                        <!-- Advanced AI Engine Settings -->
                        <div>
                            <h4 class="font-medium text-gray-700 dark:text-gray-200 mb-2">AI Engine <span class="ml-1 px-1.5 py-0.5 text-xs bg-indigo-100 dark:bg-indigo-900/30 text-indigo-800 dark:text-indigo-200 rounded">New</span></h4>
                            <div class="space-y-3">
                                <div>
                                    <label class="flex items-center space-x-2">
                                        <input type="checkbox" id="use-agentic-ai" class="rounded text-primary focus:ring-primary" checked>
                                        <span class="text-gray-700 dark:text-gray-300">Enable Groq Compound Beta Agentic AI</span>
                                    </label>
                                    <p class="text-xs text-gray-600 dark:text-gray-400 mt-1 ml-6">Leverage real-time information and code execution for more accurate prompts</p>
                                </div>
                                <div class="ml-6 space-y-2">
                                    <div>
                                        <label for="agentic-model" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Agentic AI Model</label>
                                        <select id="agentic-model" class="w-full px-3 py-2 text-base rounded-md border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-white input-focus">
                                            <option value="compound-beta">compound-beta (Multiple tools, Higher quality)</option>
                                            <option value="compound-beta-mini" selected>compound-beta-mini (Single tool, Lower latency)</option>
                                        </select>
                                    </div>
                                    <div>
                                        <label class="flex items-center space-x-2">
                                            <input type="checkbox" id="enable-web-search" class="rounded text-primary focus:ring-primary" checked>
                                            <span class="text-gray-700 dark:text-gray-300">Enable Web Search</span>
                                        </label>
                                        <p class="text-xs text-gray-600 dark:text-gray-400 mt-1 ml-6">Search for latest trends, visual references, and creative inspiration</p>
                                    </div>
                                    <div>
                                        <label class="flex items-center space-x-2">
                                            <input type="checkbox" id="enable-code-execution" class="rounded text-primary focus:ring-primary" checked>
                                            <span class="text-gray-700 dark:text-gray-300">Enable Code Execution</span>
                                        </label>
                                        <p class="text-xs text-gray-600 dark:text-gray-400 mt-1 ml-6">Use Python to process data, analyze trends, or generate complex prompts</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        
                        <!-- Advanced Model Parameters -->
                        <div>
                            <h4 class="font-medium text-gray-700 dark:text-gray-200 mb-2">Model Parameters</h4>
                            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                                <div>
                                    <label for="cfg-scale" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Prompt Adherence (CFG Scale)</label>
                                    <input type="range" id="cfg-scale" class="w-full" min="1" max="30" value="7">
                                    <div class="flex justify-between text-xs text-gray-600 dark:text-gray-400 mt-1">
                                        <span>Creative</span>
                                        <span id="cfg-value">7</span>
                                        <span>Precise</span>
                                    </div>
                                </div>
                                <div>
                                    <label for="steps" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Generation Steps</label>
                                    <input type="range" id="steps" class="w-full" min="20" max="100" value="30">
                                    <div class="flex justify-between text-xs text-gray-600 dark:text-gray-400 mt-1">
                                        <span>Faster</span>
                                        <span id="steps-value">30</span>
                                        <span>Detailed</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                        
                        <!-- Custom Camera Commands -->
                        <div>
                            <h4 class="font-medium text-gray-700 dark:text-gray-200 mb-2">Custom Camera Commands</h4>
                            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                                <div>
                                    <label for="custom-camera-movement" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Custom Movement</label>
                                    <input type="text" id="custom-camera-movement" class="w-full px-3 py-2 text-base rounded-md border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-white input-focus" placeholder="E.g., 'Reveal shot', 'Establishing shot'">
                                </div>
                                <div>
                                    <label for="camera-sequence" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Movement Sequence</label>
                                    <input type="text" id="camera-sequence" class="w-full px-3 py-2 text-base rounded-md border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-white input-focus" placeholder="E.g., 'start wide, then zoom in'">
                                </div>
                            </div>
                        </div>
                        
                        <!-- AI Model Selection -->
                        <div>
                            <h4 class="font-medium text-gray-700 dark:text-gray-200 mb-2">AI Assistant Settings</h4>
                            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                                <div>
                                    <label for="assistant-model" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Assistant Model</label>
                                    <select id="assistant-model" class="w-full px-3 py-2 text-base rounded-md border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-white input-focus">
                                        <option value="compound-beta" selected>Groq Compound Beta (with tools)</option>
                                        <option value="compound-beta-mini">Groq Compound Beta Mini</option>
                                    </select>
                                </div>
                                <div>
                                    <label for="creativity-level" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Creativity Level</label>
                                    <select id="creativity-level" class="w-full px-3 py-2 text-base rounded-md border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-white input-focus">
                                        <option value="balanced">Balanced (Default)</option>
                                        <option value="precise">Precise</option>
                                        <option value="creative">Creative</option>
                                        <option value="very-creative">Very Creative</option>
                                    </select>
                                </div>
                            </div>
                        </div>
                        
                        <!-- Advanced Prompt Settings -->
                        <div>
                            <h4 class="font-medium text-gray-700 dark:text-gray-200 mb-2">Advanced Prompt Settings</h4>
                            <div class="space-y-3">
                                <div>
                                    <label class="flex items-center space-x-2">
                                        <input type="checkbox" id="negative-prompt-enabled" class="rounded text-primary focus:ring-primary">
                                        <span class="text-gray-700 dark:text-gray-300">Enable Negative Prompt</span>
                                    </label>
                                </div>
                                <div id="negative-prompt-container" class="hidden">
                                    <label for="negative-prompt" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Negative Prompt</label>
                                    <textarea id="negative-prompt" rows="3" class="w-full px-3 py-2 text-base rounded-md border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-white input-focus" placeholder="Elements to avoid in the generation..."></textarea>
                                </div>
                                <div>
                                    <label class="flex items-center space-x-2">
                                        <input type="checkbox" id="add-model-params" class="rounded text-primary focus:ring-primary">
                                        <span class="text-gray-700 dark:text-gray-300">Add Model Parameters to Prompt</span>
                                    </label>
                                </div>
                            </div>
                        </div>
                        
                        <!-- Buttons -->
                        <div class="flex justify-end space-x-3 pt-3">
                            <button id="reset-advanced-options" class="px-4 py-2 bg-gray-200 hover:bg-gray-300 dark:bg-gray-700 dark:hover:bg-gray-600 text-gray-800 dark:text-white rounded-md">
                                Reset to Defaults
                            </button>
                            <button id="save-advanced-options" class="px-4 py-2 bg-primary hover:bg-secondary text-white rounded-md">
                                Save Changes
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Toast Notification Template -->
        <div id="toast-template" class="toast" style="display: none;">
            <div class="flex items-center">
                <i class="fas fa-info-circle mr-2"></i>
                <span id="toast-message">Notification message</span>
            </div>
        </div>
        
        <!-- File Import Modal -->
        <div id="import-modal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 hidden animate__animated animate__fadeIn">
            <div class="bg-white dark:bg-dark-card rounded-lg shadow-lg max-w-md w-full mx-4">
                <div class="p-5">
                    <div class="flex justify-between items-center mb-4">
                        <h3 class="text-xl font-semibold text-gray-800 dark:text-white">Import Prompts</h3>
                        <button id="close-import-modal" class="text-gray-500 hover:text-gray-700 dark:hover:text-gray-300">
                            <i class="fas fa-times text-xl"></i>
                        </button>
                    </div>
                    
                    <div class="mb-4">
                        <div class="bg-blue-50 dark:bg-blue-900/20 p-3 rounded-md text-sm text-blue-700 dark:text-blue-400 mb-4">
                            <i class="fas fa-info-circle mr-1"></i> You can import prompts from a JSON file or by pasting JSON data directly.
                        </div>
                        
                        <div class="space-y-4">
                            <div>
                                <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Upload JSON File</label>
                                <label class="flex flex-col items-center px-4 py-6 bg-white dark:bg-gray-800 text-gray-500 dark:text-gray-400 rounded-lg border-2 border-dashed border-gray-300 dark:border-gray-600 cursor-pointer hover:bg-gray-50 dark:hover:bg-gray-700">
                                    <i class="fas fa-cloud-upload-alt text-2xl mb-2"></i>
                                    <span class="text-sm">Click to upload or drag and drop</span>
                                    <input id="file-upload" type="file" accept=".json" class="hidden">
                                </label>
                            </div>
                            
                            <div class="relative">
                                <div class="absolute inset-0 flex items-center">
                                    <div class="w-full border-t border-gray-300 dark:border-gray-600"></div>
                                </div>
                                <div class="relative flex justify-center">
                                    <span class="px-2 bg-white dark:bg-dark-card text-sm text-gray-500 dark:text-gray-400">Or</span>
                                </div>
                            </div>
                            
                            <div>
                                <label for="json-text" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Paste JSON Data</label>
                                <textarea id="json-text" rows="6" class="w-full px-3 py-2 text-sm rounded-md border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-white input-focus" placeholder='[{"id":"prompt-1234","title":"Example Prompt","text":"Sample prompt text..."}]'></textarea>
                            </div>
                        </div>
                    </div>
                    
                    <div class="flex justify-end space-x-3">
                        <button id="cancel-import" class="px-4 py-2 bg-gray-200 hover:bg-gray-300 dark:bg-gray-700 dark:hover:bg-gray-600 text-gray-800 dark:text-white rounded-md">
                            Cancel
                        </button>
                        <button id="import-prompts" class="px-4 py-2 bg-primary hover:bg-secondary text-white rounded-md">
                            Import
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <script>
        // -------------------------
        // CONFIGURATION
        // -------------------------
        
        // Groq API Configuration
        // Replace with your actual Groq API key in a real application
        const GROQ_API_KEY = 'gsk_your_api_key_here';
        
        // Initialize user state and preferences
        let userState = {
            subscription: 'free', // 'free', 'pro', 'studio'
            darkMode: false,
            promptsCreated: 12,
            savedPrompts: 3,
            maxSavedPrompts: 5
        };
        
        // -------------------------
        // GROQ API INTEGRATION
        // -------------------------
        
        // Groq API Client
        const groqClient = {
            async createCompletion(messages, options = {}) {
                const model = options.model || 'compound-beta-mini';
                const stream = options.stream || false;
                const onProgress = options.onProgress || null;
                
                // In a real app, this would call the actual Groq API
                // For our demo, we'll simulate responses with a slight delay
                return new Promise((resolve) => {
                    // Simulated delay to mimic API call
                    setTimeout(() => {
                        // Here we would normally make an actual API call
                        // Instead, we return mock responses based on the input
                        
                        // Get the user's query from the last message
                        let userQuery = '';
                        for (let i = messages.length - 1; i >= 0; i--) {
                            if (messages[i].role === 'user') {
                                userQuery = messages[i].content;
                                break;
                            }
                        }
                        
                        // Generate mock response based on query type
                        let response;
                        
                        // Check if this is a prompt generation request
                        if (userQuery.includes('Create a detailed prompt')) {
                            response = generateMockPrompt(userQuery);
                        } 
                        // Check if this is a research request
                        else if (userQuery.includes('Research information about')) {
                            response = generateMockResearch(userQuery);
                        }
                        // Otherwise, generate a general response
                        else {
                            response = generateMockChatResponse(userQuery, model);
                        }
                        
                        if (stream && onProgress) {
                            // Simulate streaming by breaking response into chunks
                            const words = response.content.split(' ');
                            let streamedContent = '';
                            
                            // Send chunks with slight delays
                            for (let i = 0; i < words.length; i += 5) {
                                setTimeout(() => {
                                    streamedContent += ' ' + words.slice(i, i + 5).join(' ');
                                    
                                    onProgress({
                                        message: {
                                            content: streamedContent.trim(),
                                            role: 'assistant',
                                            executed_tools: i >= words.length - 5 ? response.executed_tools : null
                                        },
                                        status: i >= words.length - 5 ? 'complete' : 'incomplete'
                                    });
                                    
                                    // Resolve the promise after the last chunk
                                    if (i >= words.length - 5) {
                                        resolve({
                                            choices: [{
                                                message: {
                                                    content: response.content,
                                                    role: 'assistant',
                                                    executed_tools: response.executed_tools
                                                }
                                            }]
                                        });
                                    }
                                }, i * 30); // Adjust timing for more realistic effect
                            }
                        } else {
                            // Return complete response for non-streaming requests
                            resolve({
                                choices: [{
                                    message: {
                                        content: response.content,
                                        role: 'assistant',
                                        executed_tools: response.executed_tools
                                    }
                                }]
                            });
                        }
                    }, 800); // Simulated API delay
                });
            }
        };
        
        // Mock response generators
        function generateMockPrompt(query) {
            // Extract key details from the query
            const subjectMatch = query.match(/featuring "(.*?)"/);
            const subject = subjectMatch ? subjectMatch[1] : 'character';
            
            const actionMatch = query.match(/scene shows: (.*?)(?:\\n|The setting)/);
            const action = actionMatch ? actionMatch[1] : 'performing an action';
            
            const atmosphereMatch = query.match(/setting is: (.*?)(?:\\n|Use a)/);
            const atmosphere = atmosphereMatch ? atmosphereMatch[1] : 'atmospheric setting';
            
            // Generate an optimized prompt with the extracted information
            return {
                content: `[Tracking shot] A ${subject} ${action} in a ${atmosphere}. The camera follows the movement with smooth precision, capturing the intricate details and emotional intensity. [Zoom in] slowly on the subject's features, revealing their determination and focus. The lighting creates dramatic shadows and highlights, emphasizing the visual depth and texture of the scene. As the action intensifies, [Pan right] to reveal the broader environment and contextual elements. Atmospheric particles drift through shafts of light, adding dimension and mood to the composition. --aspect 16:9`,
                executed_tools: null
            };
        }
        
        function generateMockResearch(query) {
            // Extract the research subject
            const subjectMatch = query.match(/about "(.*?)"/);
            const subject = subjectMatch ? subjectMatch[1] : 'unknown subject';
            
            // Mock web search results with Tavily
            const executedTools = [
                {
                    type: 'web_search',
                    name: 'web_search',
                    input: {
                        query: `Visual characteristics of ${subject} for video generation`
                    },
                    output: {
                        results: [
                            {
                                title: `${subject} Visual Guide`,
                                url: 'https://example.com/visualguide',
                                content: 'A comprehensive guide to visual representation.'
                            },
                            {
                                title: `${subject} in Modern Media`,
                                url: 'https://example.com/modernmedia',
                                content: 'How this subject is portrayed in recent media.'
                            }
                        ]
                    }
                }
            ];
            
            // Generate markdown research output
            return {
                content: `# Research on "${subject}" for AI Video Generation\\n\\n## Visual Characteristics\\n\\n- Distinctive appearance with unique textures and forms\\n- Common color schemes include vibrant contrasts and harmonious palettes\\n- Visual motifs frequently associated with this subject include geometric patterns and natural elements\\n\\n## Recommended Approach\\n\\n- **Camera Movement**: Smooth tracking shots work best to capture the dynamic aspects\\n- **Lighting**: Consider dramatic lighting to emphasize depth and texture\\n- **Atmosphere**: Add environmental elements like particles or mist for depth\\n\\n## Style References\\n\\n- Classic representations often feature realistic details with atmospheric lighting\\n- Modern interpretations lean toward stylized simplification with bold color choices\\n- Experiment with depth of field to create focus on key elements\\n\\nThese insights should help you create more visually compelling and accurate prompts for your AI video generation.`,
                executed_tools: executedTools
            };
        }
        
        function generateMockChatResponse(query, model) {
            // Default response for generic queries
            let response = {
                content: `I can help you with that! When creating prompts for Hailuo AI video generation, it's important to be specific about visual details, camera movements, and atmosphere. For your question about ${query.split(' ').slice(-3).join(' ')}, I'd recommend focusing on clear descriptions and specific camera directions.`,
                executed_tools: null
            };
            
            // Check for specific question types and generate appropriate responses
            if (query.toLowerCase().includes('latest trends') || query.toLowerCase().includes('what are the latest')) {
                // This would trigger web search in a real implementation
                response.content = `Based on the latest information, current trends in AI video generation include:\\n\\n1. **Hyper-realistic textures** - Especially for close-ups and material interactions\\n2. **Dynamic lighting transitions** - Shifting between lighting styles within a single clip\\n3. **Mixed media aesthetics** - Combining hand-drawn elements with photorealistic rendering\\n4. **Volumetric atmosphere** - Using fog, particles, and light rays for depth\\n5. **Precise camera choreography** - Complex movement sequences with multiple transitions\\n\\nFor Hailuo AI specifically, users are seeing great results with detailed camera movement instructions and atmospheric descriptions.`;
                
                response.executed_tools = [
                    {
                        type: 'web_search',
                        name: 'web_search',
                        input: {
                            query: 'Latest trends in AI video generation 2023'
                        },
                        output: {
                            results: [
                                {
                                    title: 'AI Video Generation Trends - 2023 Report',
                                    url: 'https://example.com/ai-trends',
                                    content: 'The latest AI video generation trends show a move toward hyperrealistic textures and dynamic lighting.'
                                }
                            ]
                        }
                    }
                ];
            } else if (query.toLowerCase().includes('visual references') || query.toLowerCase().includes('references for')) {
                // This would also trigger web search
                const subject = query.includes('for a') ? query.split('for a')[1].trim() : 'subject';
                
                response.content = `Here are some key visual references for creating a ${subject}:\\n\\n## Essential Visual Elements\\n\\n- **Color Palette**: Neon blues, purples, and hot pink accents against dark backgrounds\\n- **Lighting**: Strong rim lighting, volumetric fog cutting through harsh geometric lights\\n- **Textures**: Reflective surfaces, LED displays, holographic elements\\n\\n## Camera Techniques\\n\\n- Use [Dolly shot] to move through dense urban canyons\\n- [Low angle] shots emphasize towering structures\\n- [Push in] slowly on detailed technological elements\\n\\n## Atmospheric Elements\\n\\n- Rain-slicked streets reflecting neon signs\\n- Steam/smoke rising from street vents\\n- Floating holographic displays and advertisements\\n\\nIncorporate these elements in your Hailuo prompts for authentic ${subject} aesthetics.`;
                
                response.executed_tools = [
                    {
                        type: 'web_search',
                        name: 'web_search',
                        input: {
                            query: `${subject} visual aesthetic elements for video`
                        },
                        output: {
                            results: [
                                {
                                    title: `${subject} Visual Design Guide`,
                                    url: 'https://example.com/design-guide',
                                    content: 'The essential visual elements that define this aesthetic include...'
                                }
                            ]
                        }
                    }
                ];
            } else if (query.toLowerCase().includes('compare') || query.toLowerCase().includes('comparison')) {
                // This might use both web search and code execution in a real implementation
                response.content = `# Comparison of Video Generation Models\\n\\n| Feature | Hailuo AI | RunwayML | Pika |  \\n|---------|-----------|----------|------|\n| Camera Control | Excellent | Good | Basic |\\n| Text Adherence | Very Good | Excellent | Good |\\n| Motion Smoothness | Good | Very Good | Excellent |\\n| Generation Speed | Fast | Medium | Fast |\\n| Customization | High | Medium | Low |\\n\\nHailuo AI specifically excels in camera movement control, which makes it ideal for cinematic sequences where precise camera positioning and movement are important. Its [Zoom in], [Pan left], and other camera commands provide fine-grained control that many other models lack.`;
                
                response.executed_tools = [
                    {
                        type: 'web_search',
                        name: 'web_search',
                        input: {
                            query: 'Compare Hailuo AI with other video generation models'
                        },
                        output: {
                            results: [
                                {
                                    title: 'AI Video Generator Comparison 2023',
                                    url: 'https://example.com/comparison',
                                    content: 'When comparing the top AI video generators, each has distinct advantages...'
                                }
                            ]
                        }
                    },
                    {
                        type: 'code_execution',
                        name: 'code_execution',
                        input: {
                            code: `
import pandas as pd

# Create comparison dataframe
data = {
    'Model': ['Hailuo AI', 'RunwayML', 'Pika'],
    'Camera Control': ['Excellent', 'Good', 'Basic'],
    'Text Adherence': ['Very Good', 'Excellent', 'Good'],
    'Motion Smoothness': ['Good', 'Very Good', 'Excellent'],
    'Generation Speed': ['Fast', 'Medium', 'Fast'],
    'Customization': ['High', 'Medium', 'Low']
}

# Create DataFrame
df = pd.DataFrame(data)
print(df.to_markdown(index=False))
`
                        },
                        output: {
                            output: "| Model     | Camera Control   | Text Adherence   | Motion Smoothness   | Generation Speed   | Customization   |\\n|:----------|:-----------------|:-----------------|:--------------------|:-------------------|:----------------|\\n| Hailuo AI | Excellent        | Very Good        | Good                | Fast               | High           |\\n| RunwayML  | Good             | Excellent        | Very Good           | Medium             | Medium         |\\n| Pika      | Basic            | Good             | Excellent           | Fast               | Low            |"
                        }
                    }
                ];
            }
            
            return response;
        }
        
        // -------------------------
        // UTILITY FUNCTIONS
        // -------------------------
        
        // Dark mode detection and toggle
        const themeToggle = document.getElementById('theme-toggle');
        
        function updateTheme() {
            if (document.documentElement.classList.contains('dark')) {
                themeToggle.checked = true;
                userState.darkMode = true;
            } else {
                themeToggle.checked = false;
                userState.darkMode = false;
            }
        }
        
        if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
            document.documentElement.classList.add('dark');
            updateTheme();
        }
        
        window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', event => {
            if (event.matches) {
                document.documentElement.classList.add('dark');
            } else {
                document.documentElement.classList.remove('dark');
            }
            updateTheme();
        });
        
        themeToggle.addEventListener('change', () => {
            if (themeToggle.checked) {
                document.documentElement.classList.add('dark');
            } else {
                document.documentElement.classList.remove('dark');
            }
            updateTheme();
        });
        
        // Toast notification system
        function showToast(message, type = 'info', duration = 3000) {
            const toast = document.getElementById('toast-template').cloneNode(true);
            toast.id = 'active-toast-' + Date.now();
            toast.querySelector('#toast-message').textContent = message;
            
            // Set toast color based on type
            if (type === 'success') {
                toast.style.backgroundColor = '#4CAF50';
            } else if (type === 'error') {
                toast.style.backgroundColor = '#F44336';
            } else if (type === 'warning') {
                toast.style.backgroundColor = '#FFC107';
                toast.style.color = '#333';
            }
            
            // Add to container and show
            document.getElementById('toast-container').appendChild(toast);
            toast.style.display = 'block';
            
            // Animate in
            setTimeout(() => {
                toast.classList.add('show');
            }, 10);
            
            // Remove after duration
            setTimeout(() => {
                toast.classList.remove('show');
                setTimeout(() => {
                    toast.remove();
                }, 300);
            }, duration);
        }
        
        // Generic loading state management
        function setLoading(elementId, isLoading) {
            const element = document.getElementById(elementId);
            if (element) {
                if (isLoading) {
                    element.classList.remove('hidden');
                } else {
                    element.classList.add('hidden');
                }
            }
        }
        
        // -------------------------
        // DOM ELEMENT REFERENCES
        // -------------------------
        
        // Tab navigation
        const tabStandard = document.getElementById('tab-standard');
        const tabLyrics = document.getElementById('tab-lyrics');
        const tabComparisons = document.getElementById('tab-comparisons');
        const tabAssistant = document.getElementById('tab-assistant');
        const standardSection = document.getElementById('standard-section');
        const lyricsSection = document.getElementById('lyrics-section');
        const comparisonsSection = document.getElementById('comparisons-section');
        const assistantSection = document.getElementById('assistant-section');
        
        // Standard Prompt Builder elements
        const hailuoModel = document.getElementById('hailuo-model');
        const promptStyle = document.getElementById('prompt-style');
        const cartoonStyle = document.getElementById('cartoon-style');
        const promptSubject = document.getElementById('prompt-subject');
        const promptAction = document.getElementById('prompt-action');
        const promptAtmosphere = document.getElementById('prompt-atmosphere');
        const promptAspect = document.getElementById('prompt-aspect');
        const specialEffects = document.getElementById('special-effects');
        const realismLevel = document.getElementById('realism-level');
        const realismValue = document.getElementById('realism-value');
        const btnGenerate = document.getElementById('btn-generate');
        const btnCopy = document.getElementById('btn-copy');
        const promptResult = document.getElementById('prompt-result');
        const btnResearchSubject = document.getElementById('btn-research-subject');
        const researchResults = document.getElementById('research-results');
        const researchContent = document.getElementById('research-content');
        const closeResearch = document.getElementById('close-research');
        
        // Camera controls
        const cameraButtons = document.querySelectorAll('.camera-btn');
        const cameraPush = document.getElementById('camera-push');
        const cameraPullout = document.getElementById('camera-pullout');
        const cameraLowangle = document.getElementById('camera-lowangle');
        const cameraOverhead = document.getElementById('camera-overhead');
        const cameraCloseup = document.getElementById('camera-closeup');
        const cameraDutch = document.getElementById('camera-dutch');
        const cameraSlowmo = document.getElementById('camera-slowmo');
        const cameraTimelapse = document.getElementById('camera-timelapse');
        
        // Model tips sections
        const modelTipsStandard = document.getElementById('model-tips-standard');
        const modelTipsDirector = document.getElementById('model-tips-director');
        const modelTipsLive = document.getElementById('model-tips-live');
        const modelTipsSubject = document.getElementById('model-tips-subject');
        
        // Template buttons
        const templateMusic = document.getElementById('template-music');
        const templateAction = document.getElementById('template-action');
        const templateAnime = document.getElementById('template-anime');
        const templateScifi = document.getElementById('template-scifi');
        const templateNature = document.getElementById('template-nature');
        const templateHorror = document.getElementById('template-horror');
        
        // Prompt Library
        const libraryToggle = document.getElementById('library-toggle');
        const libraryChevron = document.getElementById('library-chevron');
        const libraryContent = document.getElementById('library-content');
        const savedPrompts = document.getElementById('saved-prompts');
        const btnSavePrompt = document.getElementById('btn-save-prompt');
        const btnExportAll = document.getElementById('btn-export-all');
        const btnImportPrompts = document.getElementById('btn-import-prompts');
        const btnClearLibrary = document.getElementById('btn-clear-library');
        const btnSaveToLibrary = document.getElementById('btn-save-to-library');
        
        // AI Assistant elements
        const chatWindow = document.getElementById('chat-window');
        const chatInput = document.getElementById('chat-input');
        const btnSendMessage = document.getElementById('btn-send-message');
        const suggestedQuestions = document.querySelectorAll('.suggested-question');
        const currentAssistantModel = document.getElementById('current-assistant-model');
        
        // Subscription Modal elements
        const subscriptionBtn = document.getElementById('subscription-btn');
        const subscriptionModal = document.getElementById('subscription-modal');
        const closeSubscriptionModal = document.getElementById('close-subscription-modal');
        const planSelectionStep = document.getElementById('plan-selection-step');
        const paymentStep = document.getElementById('payment-step');
        const confirmationStep = document.getElementById('confirmation-step');
        const nextBtn = document.getElementById('next-btn');
        const backBtn = document.getElementById('back-btn');
        const selectPlanBtns = document.querySelectorAll('.select-plan-btn');
        const progressBar = document.getElementById('progress-bar');
        const step1Indicator = document.getElementById('step-1-indicator');
        const step2Indicator = document.getElementById('step-2-indicator');
        const step3Indicator = document.getElementById('step-3-indicator');
        const selectedPlanName = document.getElementById('selected-plan-name');
        const selectedPlanPrice = document.getElementById('selected-plan-price');
        const confirmedPlanName = document.getElementById('confirmed-plan-name');
        const confirmedPlanFeatures = document.getElementById('confirmed-plan-features');
        const confirmedEmail = document.getElementById('confirmed-email');
        const startUsingBtn = document.getElementById('start-using-btn');
        const freePlan = document.getElementById('free-plan');
        const proPlan = document.getElementById('pro-plan');
        const enterprisePlan = document.getElementById('enterprise-plan');
        const termsAgreement = document.getElementById('terms-agreement');
        const billingName = document.getElementById('billing-name');
        const billingCountry = document.getElementById('billing-country');
        const paymentEmail = document.getElementById('payment-email');
        
        // Account Modal elements
        const accountBtn = document.getElementById('account-btn');
        const accountModal = document.getElementById('account-modal');
        const closeAccountModal = document.getElementById('close-account-modal');
        const upgradeFromAccount = document.getElementById('upgrade-from-account');
        const signOutBtn = document.getElementById('sign-out-btn');
        
        // Advanced Options Modal elements
        const btnAdvancedOptions = document.getElementById('btn-advanced-options');
        const advancedOptionsModal = document.getElementById('advanced-options-modal');
        const closeAdvancedOptions = document.getElementById('close-advanced-options');
        const saveAdvancedOptions = document.getElementById('save-advanced-options');
        const resetAdvancedOptions = document.getElementById('reset-advanced-options');
        const useAgenticAI = document.getElementById('use-agentic-ai');
        const agenticModel = document.getElementById('agentic-model');
        const enableWebSearch = document.getElementById('enable-web-search');
        const enableCodeExecution = document.getElementById('enable-code-execution');
        const assistantModel = document.getElementById('assistant-model');
        
        // State variables
        let currentStep = 1;
        let selectedPlan = 'free';
        let promptLibrary = [];
        let currentPromptTags = [];
        
        // -------------------------
        // EVENT HANDLERS & UI LOGIC
        // -------------------------
        
        // Tab switching function
        function switchTab(tabElement, sectionElement) {
            // Reset all tabs
            [tabStandard, tabLyrics, tabComparisons, tabAssistant].forEach(tab => {
                tab.classList.remove('bg-primary', 'text-white');
                tab.classList.add('text-gray-700', 'dark:text-gray-300', 'hover:bg-gray-100', 'dark:hover:bg-gray-700');
            });
            
            // Hide all sections
            [standardSection, lyricsSection, comparisonsSection, assistantSection].forEach(section => {
                section.classList.add('hidden');
            });
            
            // Activate selected tab
            tabElement.classList.add('bg-primary', 'text-white');
            tabElement.classList.remove('text-gray-700', 'dark:text-gray-300', 'hover:bg-gray-100', 'dark:hover:bg-gray-700');
            
            // Show selected section with animation
            sectionElement.classList.remove('hidden');
            sectionElement.classList.add('animate__animated', 'animate__fadeIn');
            
            // Reset animation after it completes
            setTimeout(() => {
                sectionElement.classList.remove('animate__animated', 'animate__fadeIn');
            }, 500);
        }
        
        // Tab click handlers
        tabStandard.addEventListener('click', () => switchTab(tabStandard, standardSection));
        tabLyrics.addEventListener('click', () => switchTab(tabLyrics, lyricsSection));
        tabComparisons.addEventListener('click', () => switchTab(tabComparisons, comparisonsSection));
        tabAssistant.addEventListener('click', () => switchTab(tabAssistant, assistantSection));
        
        // Camera button toggle functionality
        cameraButtons.forEach(button => {
            button.addEventListener('click', () => {
                button.classList.toggle('active');
                updatePromptQuality();
            });
        });
        
        // Show/hide model-specific elements based on selected model
        hailuoModel.addEventListener('change', () => {
            const selectedModel = hailuoModel.value;
            
            // Hide all tips first
            modelTipsStandard.classList.add('hidden');
            modelTipsDirector.classList.add('hidden');
            modelTipsLive.classList.add('hidden');
            modelTipsSubject.classList.add('hidden');
            
            // Show selected model tips
            if (selectedModel === 'standard') {
                modelTipsStandard.classList.remove('hidden');
                document.getElementById('camera-controls-section').classList.add('hidden');
            } else if (selectedModel === 'director') {
                modelTipsDirector.classList.remove('hidden');
                document.getElementById('camera-controls-section').classList.remove('hidden');
            } else if (selectedModel === 'live') {
                modelTipsLive.classList.remove('hidden');
                document.getElementById('camera-controls-section').classList.add('hidden');
            } else if (selectedModel === 'subject') {
                modelTipsSubject.classList.remove('hidden');
                document.getElementById('camera-controls-section').classList.add('hidden');
            }
            
            updatePromptQuality();
        });
        
        // Update realism value text when slider changes
        realismLevel.addEventListener('input', () => {
            const value = parseInt(realismLevel.value);
            let description;
            
            // Define descriptions for different realism levels
            if (value <= 2) {
                description = "Cartoon/Animated";
            } else if (value <= 4) {
                description = "Stylized";
            } else if (value <= 6) {
                description = "Semi-Realistic";
            } else if (value <= 8) {
                description = "Moderately Realistic";
            } else {
                description = "Photorealistic";
            }
            
            realismValue.textContent = description;
            
            // Auto-adjust when at extremes
            if (value <= 3 && cartoonStyle.value === "") {
                // Suggest selecting a cartoon style for very stylized settings
                cartoonStyle.classList.add('ring-2', 'ring-primary', 'ring-opacity-50');
                setTimeout(() => {
                    cartoonStyle.classList.remove('ring-2', 'ring-primary', 'ring-opacity-50');
                }, 2000);
            }
            
            updatePromptQuality();
        });
        
        // Initialize realism value text
        realismLevel.dispatchEvent(new Event('input'));
        
        // Generate Prompt button handler
        btnGenerate.addEventListener('click', async () => {
            // Validate required fields
            const subject = promptSubject.value.trim();
            const action = promptAction.value.trim();
            
            if (!subject || !action) {
                showToast('Please enter both a subject and action description', 'warning');
                return;
            }
            
            // Show loading state
            setLoading('prompt-generating', true);
            promptResult.value = "";
            
            // Gather input values
            const model = hailuoModel.value;
            const style = promptStyle.value;
            const cartoon = cartoonStyle.value;
            const atmosphere = promptAtmosphere.value.trim();
            const aspect = promptAspect.value;
            const effects = specialEffects.value;
            const realism = parseInt(realismLevel.value);
            
            // Get camera movements
            const cameraMovements = getCameraMovements();
            
            try {
                // Create system message
                const messages = [
                    {
                        role: "system",
                        content: "You are an expert AI video prompt engineer specializing in creating optimized prompts for Hailuo AI video generation models."
                    },
                    {
                        role: "user",
                        content: `Create a detailed prompt for the ${model} model featuring "${subject}". 
                        The scene shows: ${action}
                        The setting is: ${atmosphere}
                        Use a ${style} visual style with ${getRealistDescription(realism)} level of realism.
                        ${cameraMovements ? `Include these camera movements: ${cameraMovements}` : ''}
                        ${effects ? `Add these special effects: ${effects}` : ''}
                        The aspect ratio should be ${aspect}.
                        Format the prompt as a flowing description without labels or sections.`
                    }
                ];
                
                // Send to Groq for processing
                const result = await groqClient.createCompletion(messages, {
                    model: agenticModel.value,
                    stream: false
                });
                
                // Get the generated prompt
                const generatedPrompt = result.choices[0].message.content;
                
                // Display the result
                promptResult.value = generatedPrompt;
                promptResult.classList.add('highlight-animation');
                setTimeout(() => {
                    promptResult.classList.remove('highlight-animation');
                }, 2000);
                
                // Update tags and quality
                updatePromptTags();
                updatePromptQuality();
                
                // Enable library buttons
                btnSavePrompt.disabled = false;
                btnSaveToLibrary.disabled = false;
                
                // Hide loading
                setLoading('prompt-generating', false);
                
                // Show success message
                showToast('Prompt generated successfully!', 'success');
                
            } catch (error) {
                console.error('Error generating prompt:', error);
                setLoading('prompt-generating', false);
                showToast('Error generating prompt: ' + (error.message || 'Unknown error'), 'error');
            }
        });
        
        // Copy button handler
        btnCopy.addEventListener('click', () => {
            const prompt = promptResult.value.trim();
            if (!prompt) {
                showToast('No prompt to copy', 'warning');
                return;
            }
            
            // Copy to clipboard
            navigator.clipboard.writeText(prompt)
                .then(() => {
                    // Show success animation
                    const originalText = btnCopy.innerHTML;
                    btnCopy.innerHTML = '<i class="fas fa-check mr-2"></i> Copied!';
                    setTimeout(() => {
                        btnCopy.innerHTML = originalText;
                    }, 2000);
                    
                    showToast('Prompt copied to clipboard', 'success');
                })
                .catch(err => {
                    showToast('Failed to copy: ' + err, 'error');
                });
        });
        
        // Update prompt quality meter based on form content
        function updatePromptQuality() {
            const subject = promptSubject.value.trim();
            const action = promptAction.value.trim();
            const atmosphere = promptAtmosphere.value.trim();
            let score = 0;
            let feedback = [];
            
            // Subject scoring
            if (subject.length > 0) {
                score += 10;
                if (subject.length > 10) score += 5;
                if (subject.length > 20) score += 5;
            } else {
                feedback.push("Add a subject/character");
            }
            
            // Action scoring
            if (action.length > 0) {
                score += 10;
                if (action.length > 20) score += 5;
                if (action.length > 50) score += 5;
                if (action.length > 100) score += 5;
            } else {
                feedback.push("Describe the action/scene");
            }
            
            // Atmosphere scoring
            if (atmosphere.length > 0) {
                score += 10;
                if (atmosphere.length > 20) score += 5;
                if (atmosphere.length > 50) score += 5;
            } else {
                feedback.push("Add atmosphere and setting details");
            }
            
            // Camera controls scoring (if using Director model)
            if (hailuoModel.value === 'director') {
                const activeCameraCount = document.querySelectorAll('.camera-btn.active').length;
                score += Math.min(activeCameraCount * 5, 15);
                
                if (activeCameraCount === 0) {
                    feedback.push("Add camera movements for better results");
                }
                
                // Camera checkbox options
                const cameraCheckCount = [cameraPush, cameraPullout, cameraLowangle, cameraOverhead, cameraCloseup, cameraDutch, cameraSlowmo, cameraTimelapse]
                    .filter(checkbox => checkbox.checked).length;
                
                score += Math.min(cameraCheckCount * 2, 10);
            }
            
            // Special effects scoring
            if (specialEffects.value && specialEffects.value !== "") {
                score += 10;
            } else {
                feedback.push("Consider adding special effects");
            }
            
            // Cartoon style scoring (if realism is low)
            if (parseInt(realismLevel.value) <= 4) {
                if (cartoonStyle.value && cartoonStyle.value !== "") {
                    score += 10;
                } else {
                    feedback.push("Specify a cartoon/animation style");
                }
            }
            
            // Cap the score at 100
            score = Math.min(score, 100);
            
            // Update the quality meter
            const qualityBar = document.getElementById('quality-bar');
            qualityBar.style.width = `${score}%`;
            
            // Set color based on score
            if (score < 40) {
                qualityBar.className = 'h-2 bg-red-500 rounded-full transition-all duration-500';
            } else if (score < 70) {
                qualityBar.className = 'h-2 bg-yellow-500 rounded-full transition-all duration-500';
            } else {
                qualityBar.className = 'h-2 bg-green-500 rounded-full transition-all duration-500';
            }
            
            // Update feedback text
            const qualityFeedback = document.getElementById('quality-feedback');
            
            if (score === 100) {
                qualityFeedback.innerHTML = '<p class="text-green-600 dark:text-green-400">Excellent prompt! Ready for fantastic results.</p>';
            } else if (score >= 70) {
                qualityFeedback.innerHTML = '<p class="text-green-600 dark:text-green-400">Good prompt quality. Minor improvements possible.</p>';
                if (feedback.length > 0) {
                    qualityFeedback.innerHTML += `<p class="mt-1">Suggestion: ${feedback[0]}</p>`;
                }
            } else if (score >= 40) {
                qualityFeedback.innerHTML = '<p class="text-yellow-600 dark:text-yellow-400">Average prompt. Could use more details.</p>';
                if (feedback.length > 0) {
                    const suggestions = feedback.slice(0, 2).join(', ');
                    qualityFeedback.innerHTML += `<p class="mt-1">Suggestions: ${suggestions}</p>`;
                }
            } else {
                qualityFeedback.innerHTML = '<p class="text-red-600 dark:text-red-400">Basic prompt. Needs significant improvement.</p>';
                if (feedback.length > 0) {
                    const suggestions = feedback.slice(0, 3).join(', ');
                    qualityFeedback.innerHTML += `<p class="mt-1">Suggestions: ${suggestions}</p>`;
                }
            }
            
            // Update the Save button state
            if (score >= 40 && promptResult.value.trim()) {
                btnSaveToLibrary.disabled = false;
                btnSavePrompt.disabled = false;
            } else {
                btnSaveToLibrary.disabled = true;
                btnSavePrompt.disabled = true;
            }
            
            return score;
        }
        
        // Get realism description based on slider value
        function getRealistDescription(value) {
            if (value <= 2) return "cartoon/animated style";
            if (value <= 4) return "stylized, non-photorealistic look";
            if (value <= 6) return "semi-realistic style";
            if (value <= 8) return "moderately realistic appearance";
            return "photorealistic, highly detailed style";
        }
        
        // Get camera movements from UI
        function getCameraMovements() {
            const movements = [];
            
            // Get active camera buttons
            document.querySelectorAll('.camera-btn.active').forEach(btn => {
                const cameraType = btn.dataset.camera;
                if (cameraType === 'zoom') movements.push("[Zoom in/out]");
                if (cameraType === 'pan') movements.push("[Pan left/right]");
                if (cameraType === 'tracking') movements.push("[Tracking shot]");
                if (cameraType === 'dolly') movements.push("[Dolly shot]");
                if (cameraType === 'shake') movements.push("[Shake]");
                if (cameraType === 'aerial') movements.push("[Aerial view]");
            });
            
            // Add checkbox camera options
            if (cameraPush.checked) movements.push("[Push in]");
            if (cameraPullout.checked) movements.push("[Pull out]");
            if (cameraLowangle.checked) movements.push("[Low angle]");
            if (cameraOverhead.checked) movements.push("[Overhead]");
            if (cameraCloseup.checked) movements.push("[Close-up]");
            if (cameraDutch.checked) movements.push("[Dutch angle]");
            if (cameraSlowmo.checked) movements.push("[Slow motion]");
            if (cameraTimelapse.checked) movements.push("[Time lapse]");
            
            return movements.join(", ");
        }
        
        // Update prompt tags based on content
        function updatePromptTags() {
            const subject = promptSubject.value.trim();
            const action = promptAction.value.trim();
            const atmosphere = promptAtmosphere.value.trim();
            const style = promptStyle.value;
            const cartoon = cartoonStyle.value;
            const effects = specialEffects.value;
            
            if (!subject && !action) {
                document.getElementById('prompt-tags').innerHTML = '<div class="text-xs text-gray-500 dark:text-gray-400">Fill in prompt details to generate tags</div>';
                return;
            }
            
            // Generate tags
            let tags = [];
            
            // Add style tag
            tags.push(style.replace(/-/g, ' '));
            
            // Add cartoon style if present
            if (cartoon && cartoon !== "") {
                tags.push(cartoon.replace(/-/g, ' '));
            }
            
            // Add effects if present
            if (effects && effects !== "") {
                tags.push(effects.replace(/-/g, ' '));
            }
            
            // Extract key terms from subject, action and atmosphere
            const allText = `${subject} ${action} ${atmosphere}`;
            
            // List of common keywords to look for
            const keywordList = [
                "nature", "city", "urban", "fantasy", "sci-fi", "space", "cyberpunk", "apocalyptic", 
                "beach", "mountain", "forest", "underwater", "desert", "night", "day", "sunset", 
                "sunrise", "character", "woman", "man", "child", "robot", "alien", "monster", 
                "animal", "car", "vehicle", "fight", "dance", "run", "fly", "explosion", "fire", 
                "water", "rain", "snow", "fog", "neon", "dark", "bright", "colorful", "dramatic", 
                "peaceful", "action", "slow", "fast", "horror", "romance", "adventure", "mystery", 
                "thriller", "comedy", "anime", "cartoon"
            ];
            
            // Check for keywords
            keywordList.forEach(keyword => {
                if (allText.toLowerCase().includes(keyword.toLowerCase()) && !tags.includes(keyword)) {
                    tags.push(keyword);
                }
            });
            
            // Limit tags to 6
            tags = tags.slice(0, 6);
            currentPromptTags = tags;
            
            // Update tag display
            const promptTagsContainer = document.getElementById('prompt-tags');
            promptTagsContainer.innerHTML = tags.map(tag => `
                <span class="tag">${tag}</span>
            `).join('');
        }
        
        // Research button handler
        btnResearchSubject.addEventListener('click', async () => {
            const subject = document.getElementById('preset-prompt').value.trim();
            if (!subject) {
                showToast('Please enter a subject to research', 'warning');
                return;
            }
            
            // Show research panel and loading state
            researchResults.classList.remove('hidden');
            researchContent.innerHTML = `
                <div class="flex items-center justify-center py-4">
                    <i class="fas fa-spinner fa-spin mr-2 text-primary"></i>
                    <span>Researching about "${subject}"...</span>
                </div>
            `;
            
            try {
                // Create messages for research request
                const messages = [
                    {
                        role: "system",
                        content: "You are a research assistant helping to gather visual information and references for AI video creation."
                    },
                    {
                        role: "user",
                        content: `Research information about "${subject}" that would be helpful for creating AI-generated videos. 
                        Focus on visual characteristics, popular styles, and creative approaches.
                        Include any relevant details about colors, lighting, composition, and mood.
                        Format your response with clear sections and bullet points.`
                    }
                ];
                
                // Send to Groq for processing
                const result = await groqClient.createCompletion(messages, {
                    model: 'compound-beta', // Use full compound-beta for multi-tool capability
                    stream: false
                });
                
                // Display research results with Markdown formatting
                const content = result.choices[0].message.content;
                const executedTools = result.choices[0].message.executed_tools || [];
                
                // If there were executed tools, show them in UI
                let toolsHtml = '';
                if (executedTools && executedTools.length > 0) {
                    executedTools.forEach(tool => {
                        if (tool.type === 'web_search') {
                            toolsHtml += `
                                <div class="tool-execution mb-3">
                                    <div class="tool-execution-title">
                                        <i class="fas fa-search mr-1"></i> Web Search
                                    </div>
                                    <div class="text-xs text-gray-700 dark:text-gray-300">
                                        Query: "${tool.input.query}"
                                    </div>
                                </div>
                            `;
                        } else if (tool.type === 'code_execution') {
                            toolsHtml += `
                                <div class="tool-execution mb-3">
                                    <div class="tool-execution-title">
                                        <i class="fas fa-code mr-1"></i> Code Execution
                                    </div>
                                    <div class="text-xs font-mono bg-gray-100 dark:bg-gray-800 p-2 rounded mt-1 overflow-x-auto">
                                        ${tool.input.code.replace(/</g, '&lt;').replace(/>/g, '&gt;')}
                                    </div>
                                </div>
                            `;
                        }
                    });
                }
                
                // Add the research content with Markdown formatting
                researchContent.innerHTML = toolsHtml + marked.parse(content);
                
            } catch (error) {
                console.error('Error researching subject:', error);
                researchContent.innerHTML = `
                    <div class="text-red-600 dark:text-red-400">
                        <i class="fas fa-exclamation-circle mr-1"></i>
                        Error: ${error.message || "Could not complete research. Please try again later."}
                    </div>
                `;
            }
        });
        
        // Close research panel
        closeResearch.addEventListener('click', () => {
            researchResults.classList.add('hidden');
        });
        
        // AI Assistant chat functionality
        function sendChatMessage() {
            const message = chatInput.value.trim();
            if (!message) return;
            
            // Add user message to chat
            addChatMessage('user', message);
            
            // Clear input
            chatInput.value = '';
            
            // Add loading message
            const loadingId = 'loading-' + Date.now();
            addChatMessage('assistant', '<i class="fas fa-spinner fa-spin"></i> Thinking...', loadingId);
            
            // Process chat message with Groq API
            processAIChatMessage(message, loadingId);
        }
        
        // Process AI chat message using Groq API
        async function processAIChatMessage(message, loadingId) {
            try {
                // Create system and user messages
                const messages = [
                    {
                        role: "system",
                        content: "You are Hailuo AI Assistant, an expert in helping users create effective prompts for AI video generation. Provide helpful, concise answers about Hailuo AI models, video generation techniques, and best practices for prompt creation."
                    },
                    {
                        role: "user",
                        content: message
                    }
                ];
                
                // Get current model from settings
                const model = assistantModel.value;
                
                // Process with Groq API
                const onProgress = (chunk) => {
                    if (chunk.status === 'incomplete') {
                        // Update the loading message with the current content
                        updateLoadingMessage(loadingId, marked.parse(chunk.message.content));
                    } else if (chunk.status === 'complete') {
                        // Remove loading and add final message
                        removeLoadingMessage(loadingId);
                        
                        // Check if there are executed tools to display
                        let toolsHtml = '';
                        if (chunk.message.executed_tools && chunk.message.executed_tools.length > 0) {
                            chunk.message.executed_tools.forEach(tool => {
                                if (tool.type === 'web_search') {
                                    toolsHtml += `
                                        <div class="tool-execution">
                                            <div class="tool-execution-title">
                                                <i class="fas fa-search mr-1"></i> Web Search
                                            </div>
                                            <div class="text-xs text-gray-700 dark:text-gray-300">
                                                Query: "${tool.input.query}"
                                            </div>
                                        </div>
                                    `;
                                } else if (tool.type === 'code_execution') {
                                    toolsHtml += `
                                        <div class="tool-execution">
                                            <div class="tool-execution-title">
                                                <i class="fas fa-code mr-1"></i> Code Execution
                                            </div>
                                            <div class="text-xs font-mono bg-gray-100 dark:bg-gray-800 p-2 rounded mt-1 overflow-x-auto">
                                                ${tool.input.code.replace(/</g, '&lt;').replace(/>/g, '&gt;')}
                                            </div>
                                        </div>
                                    `;
                                }
                            });
                        }
                        
                        // Add final response with tool information if available
                        addChatMessage('assistant', toolsHtml + marked.parse(chunk.message.content));
                    }
                };
                
                // Send to Groq API
                await groqClient.createCompletion(messages, {
                    model: model,
                    stream: true,
                    onProgress: onProgress
                });
                
            } catch (error) {
                console.error('Error processing chat message:', error);
                removeLoadingMessage(loadingId);
                
                // Add error message
                addChatMessage('assistant', 'Sorry, there was an error: ' + (error.message || 'An unknown error occurred'));
            }
        }
        
        // Add chat message to UI
        function addChatMessage(type, content, id = null) {
            const messageEl = document.createElement('div');
            messageEl.className = `chat-message ${type} animate__animated animate__fadeIn`;
            if (id) messageEl.id = id;
            messageEl.innerHTML = content;
            
            chatWindow.appendChild(messageEl);
            
            // Scroll to bottom
            chatWindow.scrollTop = chatWindow.scrollHeight;
            
            // Remove animation class after animation completes
            setTimeout(() => {
                messageEl.classList.remove('animate__animated', 'animate__fadeIn');
            }, 1000);
        }
        
        // Update loading message content
        function updateLoadingMessage(id, content) {
            const loadingMessage = document.getElementById(id);
            if (loadingMessage) {
                loadingMessage.innerHTML = content;
                chatWindow.scrollTop = chatWindow.scrollHeight;
            }
        }
        
        // Remove loading message
        function removeLoadingMessage(id) {
            const loadingMessage = document.getElementById(id);
            if (loadingMessage) {
                loadingMessage.remove();
            }
        }
        
        // Chat send button click handler
        btnSendMessage.addEventListener('click', sendChatMessage);
        
        // Chat input enter key handler
        chatInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                sendChatMessage();
            }
        });
        
        // Handle suggested question clicks
        suggestedQuestions.forEach(question => {
            question.addEventListener('click', () => {
                chatInput.value = question.textContent;
                sendChatMessage();
            });
        });
        
        // Library toggle
        libraryToggle.addEventListener('click', () => {
            libraryContent.classList.toggle('hidden');
            libraryChevron.classList.toggle('rotate-180');
        });
        
        // Save to library button handler
        btnSaveToLibrary.addEventListener('click', () => {
            const currentPrompt = promptResult.value.trim();
            if (!currentPrompt) {
                showToast('No prompt to save', 'warning');
                return;
            }
            
            // Check if user is on free plan and has reached limit
            if (userState.subscription === 'free' && promptLibrary.length >= userState.maxSavedPrompts) {
                showToast(`Free plan limited to ${userState.maxSavedPrompts} saved prompts. Upgrade to save more.`, 'warning');
                subscriptionBtn.classList.add('animate__animated', 'animate__pulse');
                setTimeout(() => {
                    subscriptionBtn.classList.remove('animate__animated', 'animate__pulse');
                }, 1000);
                return;
            }
            
            // Create a prompt entry
            const promptEntry = {
                id: 'prompt-' + Date.now(),
                text: currentPrompt,
                title: promptSubject.value.trim() || 'Untitled Prompt',
                tags: currentPromptTags,
                createdAt: new Date().toISOString(),
                model: hailuoModel.value,
                style: promptStyle.value
            };
            
            // Add to library
            promptLibrary.push(promptEntry);
            
            // Update library UI
            updatePromptLibrary();
            
            // Show library drawer
            libraryContent.classList.remove('hidden');
            libraryChevron.classList.add('transform', 'rotate-180');
            
            // Show success toast
            showToast('Prompt saved to library', 'success');
            
            // Enable export button
            btnExportAll.disabled = false;
        });
        
        // Update prompt library UI
        function updatePromptLibrary() {
            if (promptLibrary.length === 0) {
                savedPrompts.innerHTML = `
                    <div class="text-center text-gray-500 dark:text-gray-400 py-8 col-span-1 sm:col-span-2">
                        <i class="far fa-folder-open text-2xl mb-2"></i>
                        <p>No saved prompts yet</p>
                        <p class="text-xs mt-1">Create and save prompts to build your library</p>
                    </div>
                `;
                btnExportAll.disabled = true;
                btnClearLibrary.disabled = true;
                return;
            }
            
            // Enable buttons
            btnExportAll.disabled = false;
            btnClearLibrary.disabled = false;
            
            // Sort by newest first
            const sortedPrompts = [...promptLibrary].sort((a, b) => 
                new Date(b.createdAt) - new Date(a.createdAt)
            );
            
            // Generate prompt cards
            savedPrompts.innerHTML = sortedPrompts.map(prompt => `
                <div class="prompt-card bg-white dark:bg-gray-800 rounded-md shadow p-3 border border-light-border dark:border-dark-border hover:shadow-md transition-shadow">
                    <div class="flex justify-between items-start mb-1">
                        <h4 class="font-medium text-gray-800 dark:text-white text-sm">${prompt.title}</h4>
                        <div class="flex space-x-1">
                            <button class="load-prompt text-xs text-blue-600 dark:text-blue-400 hover:text-blue-800 dark:hover:text-blue-300" data-id="${prompt.id}">
                                <i class="fas fa-upload"></i>
                            </button>
                            <button class="delete-prompt text-xs text-red-600 dark:text-red-400 hover:text-red-800 dark:hover:text-red-300" data-id="${prompt.id}">
                                <i class="fas fa-trash"></i>
                            </button>
                        </div>
                    </div>
                    <div class="text-xs text-gray-600 dark:text-gray-400 mb-2">
                        <span class="inline-block px-1.5 py-0.5 bg-gray-100 dark:bg-gray-700 rounded mr-1">${prompt.model}</span>
                        <span class="inline-block px-1.5 py-0.5 bg-gray-100 dark:bg-gray-700 rounded">${prompt.style}</span>
                    </div>
                    <p class="text-xs text-gray-700 dark:text-gray-300 line-clamp-2">${prompt.text.substring(0, 100)}${prompt.text.length > 100 ? '...' : ''}</p>
                    ${prompt.tags && prompt.tags.length > 0 ? `
                        <div class="mt-2 flex flex-wrap gap-1">
                            ${prompt.tags.slice(0, 3).map(tag => `
                                <span class="text-xs px-1.5 py-0.5 bg-blue-50 dark:bg-blue-900/20 text-blue-700 dark:text-blue-300 rounded">${tag}</span>
                            `).join('')}
                            ${prompt.tags.length > 3 ? `<span class="text-xs px-1.5 py-0.5 bg-gray-50 dark:bg-gray-800 text-gray-500 dark:text-gray-400 rounded">+${prompt.tags.length - 3}</span>` : ''}
                        </div>
                    ` : ''}
                </div>
            `).join('');
            
            // Add event listeners to load and delete buttons
            document.querySelectorAll('.load-prompt').forEach(btn => {
                btn.addEventListener('click', (e) => {
                    const promptId = e.currentTarget.dataset.id;
                    const promptEntry = promptLibrary.find(p => p.id === promptId);
                    if (promptEntry) {
                        promptResult.value = promptEntry.text;
                        showToast(`Loaded prompt: ${promptEntry.title}`, 'success');
                    }
                });
            });
            
            document.querySelectorAll('.delete-prompt').forEach(btn => {
                btn.addEventListener('click', (e) => {
                    const promptId = e.currentTarget.dataset.id;
                    const confirmed = confirm('Are you sure you want to delete this prompt?');
                    if (confirmed) {
                        promptLibrary = promptLibrary.filter(p => p.id !== promptId);
                        updatePromptLibrary();
                        showToast('Prompt deleted', 'info');
                    }
                });
            });
            
            // Update user state
            userState.savedPrompts = promptLibrary.length;
        }
        
        // Export library button handler
        btnExportAll.addEventListener('click', () => {
            if (promptLibrary.length === 0) {
                showToast('No prompts to export', 'warning');
                return;
            }
            
            // Create export data
            const exportData = JSON.stringify(promptLibrary, null, 2);
            
            // Create blob and download link
            const blob = new Blob([exportData], {type: 'application/json'});
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'hailuo-prompt-library.json';
            a.click();
            
            // Clean up
            URL.revokeObjectURL(url);
            
            // Show toast
            showToast('Prompt library exported', 'success');
        });
        
        // Clear library button handler
        btnClearLibrary.addEventListener('click', () => {
            if (promptLibrary.length === 0) {
                showToast('Library is already empty', 'info');
                return;
            }
            
            const confirmed = confirm(`Are you sure you want to delete all ${promptLibrary.length} prompts? This cannot be undone.`);
            if (confirmed) {
                promptLibrary = [];
                updatePromptLibrary();
                showToast('Prompt library cleared', 'info');
            }
        });
        
        // Import prompts button handler
        btnImportPrompts.addEventListener('click', () => {
            document.getElementById('import-modal').classList.remove('hidden');
        });
        
        // -------------------------
        // SUBSCRIPTION MODAL LOGIC
        // -------------------------
        
        // Open subscription modal
        subscriptionBtn.addEventListener('click', () => {
            subscriptionModal.classList.remove('hidden');
            goToStep(1);
        });
        
        // Close subscription modal
        closeSubscriptionModal.addEventListener('click', () => {
            subscriptionModal.classList.add('hidden');
        });
        
        // Next button click
        nextBtn.addEventListener('click', () => {
            if (currentStep === 1) {
                // Validate plan selection
                if (!selectedPlan || selectedPlan === 'free') {
                    showToast('Please select a paid plan to continue', 'warning');
                    return;
                }
                goToStep(2);
            } else if (currentStep === 2) {
                // Validate payment info
                if (!validatePaymentForm()) {
                    return;
                }
                
                // Simulate payment processing
                nextBtn.innerHTML = '<i class="fas fa-spinner fa-spin mr-2"></i> Processing...';
                nextBtn.disabled = true;
                
                setTimeout(() => {
                    nextBtn.innerHTML = 'Continue <i class="fas fa-arrow-right ml-2"></i>';
                    nextBtn.disabled = false;
                    goToStep(3);
                    
                    // Update confirmation details
                    confirmedEmail.textContent = paymentEmail.value || 'your.email@example.com';
                    
                    // Update user subscription state
                    userState.subscription = selectedPlan;
                }, 2000);
            }
        });
        
        // Back button click
        backBtn.addEventListener('click', () => {
            if (currentStep === 2) {
                goToStep(1);
            } else if (currentStep === 3) {
                goToStep(2);
            }
        });
        
        // Select plan buttons
        selectPlanBtns.forEach(btn => {
            btn.addEventListener('click', (e) => {
                const plan = e.target.dataset.plan;
                updateSelectedPlan(plan);
            });
        });
        
        // Update selected plan UI
        function updateSelectedPlan(plan) {
            selectedPlan = plan;
            
            // Remove selected class from all plans
            freePlan.classList.remove('selected');
            proPlan.classList.remove('selected');
            enterprisePlan.classList.remove('selected');
            
            // Add selected class to chosen plan
            if (plan === 'free') {
                freePlan.classList.add('selected');
                selectedPlanName.textContent = 'Free';
                selectedPlanPrice.textContent = '$0';
                confirmedPlanName.textContent = 'Free';
                confirmedPlanFeatures.innerHTML = `
                    <li>• Basic prompt generation</li>
                    <li>• Standard AI Assistant</li>
                    <li>• Save up to 5 prompts</li>
                `;
                
                // Disable next button for free plan (already active)
                nextBtn.disabled = true;
                nextBtn.classList.add('opacity-50');
                nextBtn.title = 'Free plan is already active';
                
            } else if (plan === 'pro') {
                proPlan.classList.add('selected');
                selectedPlanName.textContent = 'Pro';
                selectedPlanPrice.textContent = '$19';
                confirmedPlanName.textContent = 'Pro';
                confirmedPlanFeatures.innerHTML = `
                    <li>• Unlimited prompt saving</li>
                    <li>• Web research with Groq</li>
                    <li>• Advanced prompt variations</li>
                    <li>• Bulk prompt generation</li>
                `;
                
                nextBtn.disabled = false;
                nextBtn.classList.remove('opacity-50');
                nextBtn.title = '';
                
            } else if (plan === 'enterprise') {
                enterprisePlan.classList.add('selected');
                selectedPlanName.textContent = 'Studio';
                selectedPlanPrice.textContent = '$49';
                confirmedPlanName.textContent = 'Studio';
                confirmedPlanFeatures.innerHTML = `
                    <li>• Team collaboration features</li>
                    <li>• Custom branding options</li>
                    <li>• API access for integration</li>
                    <li>• Priority support</li>
                    <li>• All Pro features included</li>
                `;
                
                nextBtn.disabled = false;
                nextBtn.classList.remove('opacity-50');
                nextBtn.title = '';
            }
        }
        
        // Go to specified step in subscription flow
        function goToStep(step) {
            currentStep = step;
            
            // Hide all steps
            planSelectionStep.classList.add('hidden');
            paymentStep.classList.add('hidden');
            confirmationStep.classList.add('hidden');
            
            // Reset step indicators
            step1Indicator.classList.remove('bg-primary', 'text-white');
            step1Indicator.classList.add('bg-gray-300', 'dark:bg-gray-700', 'text-gray-500', 'dark:text-gray-400');
            
            step2Indicator.classList.remove('bg-primary', 'text-white');
            step2Indicator.classList.add('bg-gray-300', 'dark:bg-gray-700', 'text-gray-500', 'dark:text-gray-400');
            
            step3Indicator.classList.remove('bg-primary', 'text-white');
            step3Indicator.classList.add('bg-gray-300', 'dark:bg-gray-700', 'text-gray-500', 'dark:text-gray-400');
            
            // Show back button for steps 2 and 3
            if (step === 1) {
                backBtn.classList.add('hidden');
                progressBar.style.width = '0%';
                
                // Activate step 1 indicator
                step1Indicator.classList.remove('bg-gray-300', 'dark:bg-gray-700', 'text-gray-500', 'dark:text-gray-400');
                step1Indicator.classList.add('bg-primary', 'text-white');
                
                // Show plan selection
                planSelectionStep.classList.remove('hidden');
                nextBtn.classList.remove('hidden');
                nextBtn.textContent = 'Continue ';
                nextBtn.innerHTML = 'Continue <i class="fas fa-arrow-right ml-2"></i>';
                
            } else if (step === 2) {
                backBtn.classList.remove('hidden');
                progressBar.style.width = '50%';
                
                // Activate step 2 indicator
                step2Indicator.classList.remove('bg-gray-300', 'dark:bg-gray-700', 'text-gray-500', 'dark:text-gray-400');
                step2Indicator.classList.add('bg-primary', 'text-white');
                
                // Show payment form
                paymentStep.classList.remove('hidden');
                nextBtn.classList.remove('hidden');
                nextBtn.textContent = 'Subscribe ';
                nextBtn.innerHTML = 'Subscribe <i class="fas fa-arrow-right ml-2"></i>';
                
            } else if (step === 3) {
                backBtn.classList.add('hidden');
                progressBar.style.width = '100%';
                
                // Activate step 3 indicator
                step3Indicator.classList.remove('bg-gray-300', 'dark:bg-gray-700', 'text-gray-500', 'dark:text-gray-400');
                step3Indicator.classList.add('bg-primary', 'text-white');
                
                // Show confirmation
                confirmationStep.classList.remove('hidden');
                nextBtn.classList.add('hidden');
            }
        }
        
        // Validate payment form
        function validatePaymentForm() {
            // Validate email
            const email = paymentEmail.value.trim();
            if (!email) {
                showToast('Please enter your email address', 'warning');
                paymentEmail.focus();
                return false;
            }
            
            if (!email.match(/^\\S+@\\S+\\.\\S+$/)) {
                showToast('Please enter a valid email address', 'warning');
                paymentEmail.focus();
                return false;
            }
            
            // Validate name
            if (!billingName.value.trim()) {
                showToast('Please enter your full name', 'warning');
                billingName.focus();
                return false;
            }
            
            // Validate country
            if (!billingCountry.value.trim()) {
                showToast('Please enter your country', 'warning');
                billingCountry.focus();
                return false;
            }
            
            // Validate terms agreement
            if (!termsAgreement.checked) {
                showToast('Please agree to the Terms of Service', 'warning');
                return false;
            }
            
            return true;
        }
        
        // Start using button (close modal, activate features)
        startUsingBtn.addEventListener('click', () => {
            subscriptionModal.classList.add('hidden');
            
            // Set max saved prompts based on plan
            if (selectedPlan === 'pro' || selectedPlan === 'enterprise') {
                userState.maxSavedPrompts = Infinity;
            }
            
            // Show toast confirmation
            showToast(`${confirmedPlanName.textContent} plan activated successfully!`, 'success');
            
            // Update the UI based on new subscription
            updateUIForSubscription();
        });
        
        // Account modal handlers
        accountBtn.addEventListener('click', () => {
            // Update account stats before showing
            updateAccountUI();
            accountModal.classList.remove('hidden');
        });
        
        closeAccountModal.addEventListener('click', () => {
            accountModal.classList.add('hidden');
        });
        
        upgradeFromAccount.addEventListener('click', () => {
            accountModal.classList.add('hidden');
            subscriptionBtn.click();
        });
        
        // Update account UI based on current state
        function updateAccountUI() {
            const savedPromptCount = document.querySelector('#account-modal .text-2xl:last-child');
            if (savedPromptCount) {
                savedPromptCount.innerHTML = `${userState.savedPrompts}<span class="text-xs font-normal text-gray-500 dark:text-gray-400">/${userState.maxSavedPrompts === Infinity ? '∞' : userState.maxSavedPrompts}</span>`;
            }
        }
        
        // Update UI elements based on subscription status
        function updateUIForSubscription() {
            if (userState.subscription === 'free') {
                // Free plan UI
                document.querySelectorAll('.pro-only-feature').forEach(el => {
                    el.classList.add('opacity-50');
                    if (el.tagName === 'BUTTON') {
                        el.setAttribute('data-pro-feature', 'true');
                    }
                });
            } else {
                // Pro/Enterprise plan UI
                document.querySelectorAll('.pro-only-feature').forEach(el => {
                    el.classList.remove('opacity-50');
                    if (el.tagName === 'BUTTON') {
                        el.removeAttribute('data-pro-feature');
                    }
                });
                
                // Enable agentic AI features
                useAgenticAI.checked = true;
                document.getElementById('agentic-capabilities-banner').classList.remove('hidden');
                document.getElementById('compound-beta-info').classList.remove('hidden');
                document.getElementById('agentic-questions').classList.remove('hidden');
                
                // Update the subscription UI
                subscriptionBtn.innerHTML = `<i class="fas fa-crown mr-1"></i> ${userState.subscription.charAt(0).toUpperCase() + userState.subscription.slice(1)}`;
                subscriptionBtn.classList.add('bg-gradient-to-r', 'from-indigo-600', 'to-purple-600');
            }
        }
        
        // Advanced Options Modal
        btnAdvancedOptions.addEventListener('click', () => {
            advancedOptionsModal.classList.remove('hidden');
        });
        
        closeAdvancedOptions.addEventListener('click', () => {
            advancedOptionsModal.classList.add('hidden');
        });
        
        // Save advanced options
        saveAdvancedOptions.addEventListener('click', () => {
            advancedOptionsModal.classList.add('hidden');
            
            // Apply settings
            if (useAgenticAI.checked) {
                // Update assistant model display
                if (assistantModel.value.includes('compound-beta')) {
                    currentAssistantModel.textContent = 'Groq Compound Beta';
                    document.getElementById('agentic-capabilities-banner').classList.remove('hidden');
                    document.getElementById('compound-beta-info').classList.remove('hidden');
                    document.getElementById('agentic-questions').classList.remove('hidden');
                    
                    // Show specific capabilities based on enabled features
                    document.getElementById('search-capability').classList.toggle('hidden', !enableWebSearch.checked);
                    document.getElementById('code-capability').classList.toggle('hidden', !enableCodeExecution.checked);
                } else {
                    currentAssistantModel.textContent = assistantModel.value;
                    document.getElementById('agentic-capabilities-banner').classList.add('hidden');
                    document.getElementById('compound-beta-info').classList.add('hidden');
                    document.getElementById('agentic-questions').classList.add('hidden');
                }
                
                showToast('Advanced options saved', 'success');
            } else {
                // User disabled agentic AI
                document.getElementById('agentic-capabilities-banner').classList.add('hidden');
                document.getElementById('compound-beta-info').classList.add('hidden');
                document.getElementById('agentic-questions').classList.add('hidden');
                currentAssistantModel.textContent = assistantModel.value;
                
                showToast('Advanced options saved (Agentic AI disabled)', 'info');
            }
        });
        
        // Agentic AI toggle
        useAgenticAI.addEventListener('change', () => {
            // Update UI elements based on toggle
            if (useAgenticAI.checked) {
                enableWebSearch.parentElement.classList.remove('opacity-50');
                enableCodeExecution.parentElement.classList.remove('opacity-50');
                enableWebSearch.disabled = false;
                enableCodeExecution.disabled = false;
                agenticModel.disabled = false;
            } else {
                enableWebSearch.parentElement.classList.add('opacity-50');
                enableCodeExecution.parentElement.classList.add('opacity-50');
                enableWebSearch.disabled = true;
                enableCodeExecution.disabled = true;
                agenticModel.disabled = true;
            }
        });
        
        // Reset advanced options
        resetAdvancedOptions.addEventListener('click', () => {
            // Reset form values
            useAgenticAI.checked = true;
            agenticModel.value = 'compound-beta-mini';
            enableWebSearch.checked = true;
            enableCodeExecution.checked = true;
            
            document.getElementById('cfg-scale').value = 7;
            document.getElementById('cfg-value').textContent = "7";
            document.getElementById('steps').value = 30;
            document.getElementById('steps-value').textContent = "30";
            
            document.getElementById('negative-prompt-enabled').checked = false;
            document.getElementById('negative-prompt-container').classList.add('hidden');
            document.getElementById('negative-prompt').value = "";
            
            document.getElementById('add-model-params').checked = false;
            document.getElementById('custom-camera-movement').value = "";
            document.getElementById('camera-sequence').value = "";
            
            document.getElementById('assistant-model').value = 'compound-beta';
            document.getElementById('creativity-level').value = 'balanced';
            
            // Ensure UI reflects changes
            useAgenticAI.dispatchEvent(new Event('change'));
            
            showToast('Settings reset to defaults', 'info');
        });
        
        // -------------------------
        // TEMPLATE HANDLERS
        // -------------------------
        
        // Template handlers
        templateMusic.addEventListener('click', () => {
            hailuoModel.value = 'director';
            promptStyle.value = 'music-video';
            cartoonStyle.value = '';
            promptSubject.value = "Character in a dodge charger with a mounted machine gun";
            promptAction.value = "Character chases a man in a flannel shirt, shooting at his feet while bullets fly around. Fast cuts between the chase and close-ups of the character.";
            promptAtmosphere.value = "Urban setting with neon lights, rain-soaked streets with graffiti. Surreal, psychedelic atmosphere with distorted cityscapes and electric colors.";
            specialEffects.value = "neon";
            realismLevel.value = 7;
            realismLevel.dispatchEvent(new Event('input'));
            
            // Reset camera buttons
            cameraButtons.forEach(btn => btn.classList.remove('active'));
            
            // Set active camera buttons
            document.querySelector('[data-camera="zoom"]').classList.add('active');
            document.querySelector('[data-camera="tracking"]').classList.add('active');
            document.querySelector('[data-camera="shake"]').classList.add('active');
            
            // Reset camera checkboxes
            cameraPush.checked = false;
            cameraPullout.checked = false;
            cameraLowangle.checked = false;
            cameraOverhead.checked = false;
            cameraCloseup.checked = true;
            cameraDutch.checked = false;
            cameraSlowmo.checked = false;
            cameraTimelapse.checked = false;
            
            // Update model tips visibility
            hailuoModel.dispatchEvent(new Event('change'));
            
            // Update quality meter
            updatePromptQuality();
            
            // Show toast notification
            showToast("Music Video template loaded", "success");
        });
        
        templateAction.addEventListener('click', () => {
            hailuoModel.value = 'director';
            promptStyle.value = 'action';
            cartoonStyle.value = '';
            promptSubject.value = "Character with an RPG launcher";
            promptAction.value = "An intense fight scene with the character shooting an RPG at enemies. The weapon fires with a dramatic explosion and impact.";
            promptAtmosphere.value = "Gritty urban environment with smoky atmosphere. Dramatic lighting with high contrast between shadows and highlights.";
            specialEffects.value = "fire";
            realismLevel.value = 8;
            realismLevel.dispatchEvent(new Event('input'));
            
            // Reset camera buttons
            cameraButtons.forEach(btn => btn.classList.remove('active'));
            
            // Set active camera buttons
            document.querySelector('[data-camera="pan"]').classList.add('active');
            document.querySelector('[data-camera="tracking"]').classList.add('active');
            document.querySelector('[data-camera="shake"]').classList.add('active');
            
            // Reset camera checkboxes
            cameraPush.checked = true;
            cameraPullout.checked = false;
            cameraLowangle.checked = true;
            cameraOverhead.checked = false;
            cameraCloseup.checked = true;
            cameraDutch.checked = true;
            cameraSlowmo.checked = true;
            cameraTimelapse.checked = false;
            
            // Update model tips visibility
            hailuoModel.dispatchEvent(new Event('change'));
            
            // Update quality meter
            updatePromptQuality();
            
            // Show toast notification
            showToast("Action Sequence template loaded", "success");
        });
        
        templateAnime.addEventListener('click', () => {
            hailuoModel.value = 'standard';
            promptStyle.value = 'anime';
            cartoonStyle.value = 'shounen-anime';
            promptSubject.value = "Anime character with bright colorful hair";
            promptAction.value = "Character in dynamic pose with energy effects surrounding them. Fast, fluid movements with anime-style exaggeration.";
            promptAtmosphere.value = "Stylized background with speed lines and vibrant colors. High contrast lighting with dramatic shadows.";
            specialEffects.value = "energy-aura";
            realismLevel.value = 3;
            realismLevel.dispatchEvent(new Event('input'));
            
            // Update model tips visibility
            hailuoModel.dispatchEvent(new Event('change'));
            
            // Update quality meter
            updatePromptQuality();
            
            // Show toast notification
            showToast("Anime Style template loaded", "success");
        });
        
        templateScifi.addEventListener('click', () => {
            hailuoModel.value = 'director';
            promptStyle.value = 'sci-fi';
            cartoonStyle.value = '';
            promptSubject.value = "Astronaut explorer in high-tech spacesuit";
            promptAction.value = "Explorer walking through an alien landscape with glowing flora, discovering ancient alien technology embedded in rock formations.";
            promptAtmosphere.value = "Alien planet with strange rock formations and two moons visible in the purple-hued sky. Bioluminescent plants emit eerie blue light.";
            specialEffects.value = "hologram";
            realismLevel.value = 9;
            realismLevel.dispatchEvent(new Event('input'));
            
            // Reset camera buttons
            cameraButtons.forEach(btn => btn.classList.remove('active'));
            
            // Set active camera buttons
            document.querySelector('[data-camera="pan"]').classList.add('active');
            document.querySelector('[data-camera="aerial"]').classList.add('active');
            
            // Reset camera checkboxes
            cameraPush.checked = true;
            cameraPullout.checked = false;
            cameraLowangle.checked = false;
            cameraOverhead.checked = true;
            cameraCloseup.checked = false;
            cameraDutch.checked = false;
            cameraSlowmo.checked = false;
            cameraTimelapse.checked = false;
            
            // Update model tips visibility
            hailuoModel.dispatchEvent(new Event('change'));
            
            // Update quality meter
            updatePromptQuality();
            
            // Show toast notification
            showToast("Sci-Fi Explorer template loaded", "success");
        });
        
        // Initialize the application
        function initializeApp() {
            // Set default tab
            switchTab(tabStandard, standardSection);
            
            // Initialize the theme based on system preference
            updateTheme();
            
            // Initialize prompt quality meter
            updatePromptQuality();
            
            // Set default plan
            updateSelectedPlan('free');
            
            // Update UI based on subscription status (free by default)
            updateUIForSubscription();
            
            // Show welcome toast
            setTimeout(() => {
                showToast('Welcome to Hailuo AI Video Prompt Builder!', 'info');
            }, 1000);
        }
        
        // Run initialization
        initializeApp();
    </script>
</body>
</html>''')

# Create an __init__.py file
with open('hailuo_prompt_builder/__init__.py', 'w') as f:
    f.write('# Hailuo AI Video Prompt Builder Pro\n')

# Create a simple Flask server to serve the application
with open('hailuo_prompt_builder/server.py', 'w') as f:
    f.write('''from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
''')

# Create a README.md file
with open('README.md', 'w') as f:
    f.write('''# Hailuo AI Video Prompt Builder Pro

A premium tool designed for creating optimized prompts for MiniMax Hailuo AI video generation models.

## Overview

The Hailuo AI Video Prompt Builder Pro is a premium tool designed for creators who want to generate professional-quality prompts for MiniMax Hailuo AI video generation models. This advanced application streamlines the complex process of crafting effective video prompts with AI-assisted features, visual previews, and extensive customization options.

## Key Features

### Core Functionality

- **Multi-Model Support**: Compatible with all Hailuo AI models (Standard, Director, Live, Subject)
- **Prompt Library**: Save, organize, and retrieve your prompts with tagging and search
- **AI Configuration Assistant**: Automatically generate optimal settings based on simple descriptions
- **Prompt Quality Analysis**: Real-time feedback on prompt effectiveness with improvement suggestions
- **Prompt Amplification**: Enhance existing prompts with more vivid details and improved structure
- **Visual Preview**: See concept images of your prompt before generating videos
- **Dark/Light Mode**: Comfortable viewing in any environment

### Advanced Tools

- **Research Assistant**: AI-powered research for visual references and creative inspiration
- **Compare & Remix**: Generate multiple prompt variations and compare them side by side
- **Lyrics Visualizer**: Break down song lyrics into video segments for complete music videos
- **AI Assistant**: Dedicated assistant with web search and code execution capabilities
- **Advanced Camera Controls**: Precise camera movement sequencing for cinematic results
- **Comprehensive Style Library**: Extensive selection of visual styles, effects, and animation types

