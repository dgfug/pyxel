#ifndef PYXELCORE_SYSTEM_H_
#define PYXELCORE_SYSTEM_H_

#include <cstdint>
#include <string>

class SDL_Renderer;
class SDL_Window;
class SDL_Texture;

namespace pyxelcore {

class Canvas;
class Tilemap;

class System {
 public:
  System(int32_t width,
         int32_t height,
         const char* caption = NULL,
         int32_t scale = -1,
         const int32_t* palette = NULL,
         int32_t fps = -1,
         int32_t border_width = -1,
         int32_t border_color = -1);
  ~System();

  Canvas* Screen() { return screen_; }

  int32_t Width() { return width_; }
  int32_t Height() { return height_; }
  int32_t FrameCount() { return frame_count_; }

  Canvas* GetImage(int32_t img, bool system = false);
  Tilemap* GetTilemap(int32_t tm);

  void RunApplication(void (*update)(), void (*draw)());
  void QuitApplication();

  void LoadImage(Canvas* image, int32_t x, int32_t y, const char* filename);
  void LoadAsset(const char* filename);
  void SaveAsset(const char* filename);

 private:
  int32_t width_;
  int32_t height_;
  std::string caption_;
  int32_t scale_;
  int32_t palette_[16];
  int32_t fps_;
  int32_t border_width_;
  int32_t border_color_;
  int32_t frame_count_;

  Canvas* screen_;
  Canvas** image_;
  Tilemap** tilemap_;

  SDL_Renderer* renderer_;
  SDL_Window* window_;
  SDL_Texture* screen_texture_;

  void UpdateScreenTexture();
};

}  // namespace pyxelcore

#endif  // PYXELCORE_SYSTEM_H_
