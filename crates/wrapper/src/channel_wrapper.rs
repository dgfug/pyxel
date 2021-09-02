use pyo3::prelude::*;

use pyxel::SharedChannel as PyxelSharedChannel;
use pyxel::Volume;

use crate::instance;
use crate::sound_wrapper::Sound;

#[pyclass]
#[derive(Clone)]
pub struct Channel {
    pub pyxel_channel: PyxelSharedChannel,
}

pub fn wrap_pyxel_channel(pyxel_channel: PyxelSharedChannel) -> Channel {
    Channel { pyxel_channel }
}

#[pymethods]
impl Channel {
    #[getter]
    pub fn get_volume(&self) -> PyResult<Volume> {
        Ok(self.pyxel_channel.lock().volume)
    }

    #[setter]
    pub fn set_volume(&self, volume: Volume) -> PyResult<()> {
        self.pyxel_channel.lock().volume = volume;

        Ok(())
    }

    pub fn play_pos(&self) -> PyResult<Option<(u32, u32)>> {
        Ok(self.pyxel_channel.lock().play_pos())
    }

    #[pyo3(text_signature = "($self, snd, *, loop)")]
    pub fn play(&self, snd: &PyAny, r#loop: Option<bool>) -> PyResult<()> {
        let loop_ = r#loop.unwrap_or(false);

        type_switch! {
            snd,
            u32,
            {
                self.pyxel_channel
                    .lock()
                    .play1(instance().sound(snd).lock().clone(), loop_);
            },
            Vec<u32>,
            {
                let snd = snd
                    .iter()
                    .map(|sound_no| instance().sound(*sound_no).lock().clone())
                    .collect();

                self.pyxel_channel.lock().play(snd, loop_);
            },
            Sound,
            {
                self.pyxel_channel
                    .lock()
                    .play1(snd.pyxel_sound.lock().clone(), loop_);
            },
            Vec<Sound>,
            {
                let snd = snd
                    .iter()
                    .map(|sound| sound.pyxel_sound.lock().clone())
                    .collect();

                self.pyxel_channel.lock().play(snd, loop_);
            }
        }

        Ok(())
    }

    pub fn stop(&mut self) -> PyResult<()> {
        self.pyxel_channel.lock().stop();

        Ok(())
    }
}

pub fn add_channel_class(m: &PyModule) -> PyResult<()> {
    m.add_class::<Channel>()?;

    Ok(())
}
