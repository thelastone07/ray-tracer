#include<iostream>
#include<chrono>

#include "utility/color.h"

signed main() {
    // camera
    int image_width = 256;
    int image_height = 256;

    auto start = std::chrono::high_resolution_clock::now();

    std::cout << "P3\n" << image_height << " " << image_width << "\n255\n";
    
    for (int j = 0; j < image_height; j++) {
        std::clog << "\rRemaining: " << image_height - j << " " << std::flush;
        for (int i = 0; i < image_width; i++) {
            write_color(std::cout, color(double(i) / (image_width-1), double(j) / (image_height - 1), 0));
        }
    }
    std::clog << "\rDone                       \n";
    auto end = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
    std::clog << "\nRender time: " << duration.count() << " ms\n";
}