#!/usr/bin/python3

import subprocess

def run_free_command():
    """freeコマンドを実行してメモリ使用状況を表示"""
    try:
        result = subprocess.run(['free', '-h'], capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"freeコマンドの実行に失敗しました: {e}")

def main():
    print("=== メモリ獲得前のメモリ使用状況 ===")
    run_free_command()
    
    # 100MB程度のメモリを獲得
    print("100MBのメモリを獲得中...")
    memory_size = 100 * 1024 * 1024  # 100MB
    memory_buffer = bytearray(memory_size)
    
    # メモリを実際に使用するために書き込み
    for i in range(0, memory_size, 1024):
        memory_buffer[i] = 1
    
    print("=== メモリ獲得後のメモリ使用状況 ===")
    run_free_command()
    
    print("メモリ獲得完了。プログラムを終了します。")

if __name__ == "__main__":
    main()