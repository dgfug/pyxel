#ifndef PYXELCORE_H_
#define PYXELCORE_H_

#ifdef __cplusplus
extern "C" {
#endif

#ifdef WIN32
#ifdef PYXEL_DLL
#define PYXEL_API __declspec(dllexport)
#else
#define PYXEL_API __declspec(dllimport)
#endif
#else
#define PYXEL_API
#endif

//
// System
//
PYXEL_API int get_width();
PYXEL_API int get_height();
PYXEL_API int get_frame_count();

PYXEL_API void init(int width, int height, char *caption, int scale,
                    int *palette, int fps, int border_width, int border_color);
PYXEL_API void run(void (*update)(), void (*draw)());
PYXEL_API void quit();

//
// Resource
//
PYXEL_API void save(char *filename);
PYXEL_API void load(char *filename);

//
// Input
//
PYXEL_API int get_mouse_x();
PYXEL_API int get_mouse_y();

PYXEL_API int btn(int key);
PYXEL_API int btnp(int key, int hold, int period);
PYXEL_API int btnr(int key);
PYXEL_API void mouse(int visible);

//
// Graphics
//
PYXEL_API void *image(int img, int system);
PYXEL_API void *tilemap(int tm);
PYXEL_API void clip(int x1, int y1, int x2, int y2);
PYXEL_API void pal(int col1, int col2);
PYXEL_API void cls(int col);
PYXEL_API void pix(int x, int y, int col);
PYXEL_API void line(int x1, int y1, int x2, int y2, int col);
PYXEL_API void rect(int x1, int y1, int x2, int y2, int col);
PYXEL_API void rectb(int x1, int y1, int x2, int y2, int col);
PYXEL_API void circ(int x, int y, int r, int col);
PYXEL_API void circb(int x, int y, int r, int col);
PYXEL_API void blt(int x, int y, int img, int u, int v, int w, int h,
                   int colkey);
PYXEL_API void bltm(int x, int y, int tm, int u, int v, int w, int h,
                    int colkey);
PYXEL_API void text(int x, int y, int s, int col);

//
// Audio
//
PYXEL_API void *sound(int snd, int system);
PYXEL_API void *music(int msc);
PYXEL_API void play(int ch, int snd, int loop);
PYXEL_API void playm(int msc, int loop);
PYXEL_API void stop(int ch);

//
// Image class
//
PYXEL_API int get_Image_width(void *self);
PYXEL_API int get_Image_height(void *self);
PYXEL_API int *get_Image_data(void *self);

PYXEL_API int Image_get(void *self, int x, int y);
PYXEL_API void Image_set1(void *self, int x, int y, int data);
PYXEL_API void Image_set(void *self, int x, int y, int *data, int data_width,
                         int data_height);
PYXEL_API void Image_load(void *self, int x, int y, char *filename);
PYXEL_API void Image_copy(void *self, int x, int y, int img, int u, int v,
                          int w, int h);

//
// Tilemap class
//
PYXEL_API int get_Tilemap_width(void *self);
PYXEL_API int get_Tilemap_height(void *self);
PYXEL_API int *get_Tilemap_data(void *self);

PYXEL_API int Tilemap_get(int x, int y);
PYXEL_API void Timemap_set1(int x, int y, int data, int refimg);
PYXEL_API void Timemap_set(int x, int y, int *data, int data_width,
                           int data_height, int refimg);
PYXEL_API void Timemap_copy(int x, int y, int tm, int u, int v, int w, int h);

//
// Sound class
//
PYXEL_API int *get_Sound_note(void *self, int *length);
PYXEL_API void set_Sound_note(void *self, int length);
PYXEL_API int *get_Sound_tone(void *self, int *length);
PYXEL_API void set_Sound_tone(void *self, int length);
PYXEL_API int *get_Sound_volume(void *self, int *length);
PYXEL_API void set_Sound_volume(void *self, int length);
PYXEL_API int *get_Sound_effect(void *self, int *length);
PYXEL_API void set_Sound_effect(void *self, int length);
PYXEL_API int get_Sound_speed(void *self);
PYXEL_API void set_Sound_speed(void *self, int speed);

PYXEL_API void Sound_set(void *self, char *note, char *tone, char *volume,
                         char *effect, int speed);
PYXEL_API void Sound_set_note(void *self, char *data);
PYXEL_API void Sound_set_tone(void *self, char *data);
PYXEL_API void Sound_set_volume(void *self, char *data);
PYXEL_API void Sound_set_effect(void *self, char *data);

//
// Music class
//
PYXEL_API int *get_Music_ch0(void *self, int *length);
PYXEL_API void set_Music_ch0(void *self, int length);
PYXEL_API int *get_Music_ch1(void *self, int *length);
PYXEL_API void set_Music_ch1(void *self, int length);
PYXEL_API int *get_Music_ch2(void *self, int *length);
PYXEL_API void set_Music_ch2(void *self, int length);
PYXEL_API int *get_Music_ch3(void *self, int *length);
PYXEL_API void set_Music_ch3(void *self, int length);

PYXEL_API void Music_set(void *self, int *ch0, int ch0_length, int *ch1,
                         int ch1_length, int *ch2, int ch2_length, int *ch3,
                         int ch3_length);
PYXEL_API void Music_set_ch0(void *self, int *data, int data_length);
PYXEL_API void Music_set_ch1(void *self, int *data, int data_length);
PYXEL_API void Music_set_ch2(void *self, int *data, int data_length);
PYXEL_API void Music_set_ch3(void *self, int *data, int data_length);

#ifdef __cplusplus
}
#endif

#endif // PYXELCORE_H_
