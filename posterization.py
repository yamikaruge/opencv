# -*- coding: utf-8 -*-

import cv2
import numpy as np

if __name__ == '__main__':

    # ルックアップテーブルを作成するため変数の定義
    solarization_const = 2 * np.pi / 255

    # ルックアップテーブルの生成
    """
    array([[0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
        ・・・・・・・・
           [0], dtype='uint8')
    のようなリストが生成される。
    """
    look_up_table = np.ones((256, 1), dtype = 'uint8' ) * 0

    for i in range(256):

        if i < 64:
        
          look_up_table[i][0] = 0

        elif i < 128:

          look_up_table[i][0] = 100

        elif i < 192:

          look_up_table[i][0] = 200

        else:

          look_up_table[i][0] = 300

    # 画像の読み込み
    img_src = cv2.imread("./image/sora2.jpg", 1)

    # ソラリゼーション後の出力
    img_post = cv2.LUT(img_src, look_up_table)

    # 表示
    cv2.imshow("Show POSTERIZATION Image", img_post)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
