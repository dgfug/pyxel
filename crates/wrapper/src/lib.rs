#[macro_use]
mod utility;
mod audio_wrapper;
mod channel_wrapper;
mod constant_wrapper;
mod graphics_wrapper;
mod image_wrapper;
mod input_wrapper;
mod music_wrapper;
mod resource_wrapper;
mod sound_wrapper;
mod system_wrapper;
mod tilemap_wrapper;
#[allow(non_snake_case)]
mod variable_wrapper;

use pyo3::prelude::*;
use pyo3::types::PyDict;
use std::mem::transmute;

use pyxel::Pyxel;

use crate::audio_wrapper::add_audio_functions;
use crate::channel_wrapper::add_channel_class;
use crate::constant_wrapper::add_module_constants;
use crate::graphics_wrapper::add_graphics_functions;
use crate::image_wrapper::add_image_class;
use crate::input_wrapper::add_input_functions;
use crate::music_wrapper::add_music_class;
use crate::resource_wrapper::add_resource_functions;
use crate::sound_wrapper::add_sound_class;
use crate::system_wrapper::add_system_functions;
use crate::tilemap_wrapper::add_tilemap_class;
use crate::variable_wrapper::add_module_variables;

static mut INSTANCE: *mut Pyxel = 0 as *mut Pyxel;

pub fn instance() -> &'static mut Pyxel {
    unsafe {
        if INSTANCE != 0 as *mut Pyxel {
            &mut *INSTANCE
        } else {
            panic!("Pyxel is not initialized");
        }
    }
}

pub fn set_instance(pyxel: Pyxel) {
    unsafe {
        INSTANCE = transmute(Box::new(pyxel));
    }
}

pub fn set_current_directory(py: Python) -> PyResult<()> {
    let locals = PyDict::new(py);
    locals.set_item("os", py.import("os")?)?;
    locals.set_item("inspect", py.import("inspect")?)?;
    py.eval(
        "os.chdir(os.path.dirname(inspect.stack()[-1].filename))",
        None,
        Some(&locals),
    )?;

    Ok(())
}

#[pymodule]
fn pyxel_wrapper(py: Python, m: &PyModule) -> PyResult<()> {
    add_image_class(m)?;
    add_tilemap_class(m)?;
    add_channel_class(m)?;
    add_sound_class(m)?;
    add_music_class(m)?;

    add_module_constants(m)?;
    add_module_variables(m)?;

    add_system_functions(m)?;
    add_resource_functions(m)?;
    add_input_functions(m)?;
    add_graphics_functions(m)?;
    add_audio_functions(m)?;

    set_current_directory(py)?;

    Ok(())
}
