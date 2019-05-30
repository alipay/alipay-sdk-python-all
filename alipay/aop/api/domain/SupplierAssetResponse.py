#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SupplierAssetResponse(object):

    def __init__(self):
        self._approval_remark = None
        self._approval_status = None
        self._approval_status_text = None
        self._bluetooth_mode = None
        self._bluetooth_mode_text = None
        self._contact_address = None
        self._contact_mobile = None
        self._contact_name = None
        self._cpu = None
        self._device_design_img = None
        self._device_design_img_id = None
        self._device_img = None
        self._device_img_id = None
        self._device_name = None
        self._device_other_desc = None
        self._face_camera = None
        self._gmt_create = None
        self._gmt_modified = None
        self._id = None
        self._item_id = None
        self._line_network_mode = None
        self._line_network_mode_text = None
        self._memory = None
        self._min_os_version = None
        self._model_number = None
        self._network_mode = None
        self._network_mode_text = None
        self._os_type = None
        self._printer = None
        self._ram = None
        self._rom = None
        self._scan_code_mode = None
        self._scan_code_read_dista = None
        self._screen_dpi = None
        self._screen_size = None
        self._sdk_auto_file = None
        self._sdk_auto_file_id = None
        self._sdk_name = None
        self._sdk_version = None
        self._storage = None
        self._supplier_name = None
        self._supplier_pid = None
        self._supplier_sn = None
        self._tranaction_model = None
        self._tranaction_model_text = None
        self._wifi_mode = None
        self._wifi_mode_text = None

    @property
    def approval_remark(self):
        return self._approval_remark

    @approval_remark.setter
    def approval_remark(self, value):
        self._approval_remark = value
    @property
    def approval_status(self):
        return self._approval_status

    @approval_status.setter
    def approval_status(self, value):
        self._approval_status = value
    @property
    def approval_status_text(self):
        return self._approval_status_text

    @approval_status_text.setter
    def approval_status_text(self, value):
        self._approval_status_text = value
    @property
    def bluetooth_mode(self):
        return self._bluetooth_mode

    @bluetooth_mode.setter
    def bluetooth_mode(self, value):
        self._bluetooth_mode = value
    @property
    def bluetooth_mode_text(self):
        return self._bluetooth_mode_text

    @bluetooth_mode_text.setter
    def bluetooth_mode_text(self, value):
        self._bluetooth_mode_text = value
    @property
    def contact_address(self):
        return self._contact_address

    @contact_address.setter
    def contact_address(self, value):
        self._contact_address = value
    @property
    def contact_mobile(self):
        return self._contact_mobile

    @contact_mobile.setter
    def contact_mobile(self, value):
        self._contact_mobile = value
    @property
    def contact_name(self):
        return self._contact_name

    @contact_name.setter
    def contact_name(self, value):
        self._contact_name = value
    @property
    def cpu(self):
        return self._cpu

    @cpu.setter
    def cpu(self, value):
        self._cpu = value
    @property
    def device_design_img(self):
        return self._device_design_img

    @device_design_img.setter
    def device_design_img(self, value):
        self._device_design_img = value
    @property
    def device_design_img_id(self):
        return self._device_design_img_id

    @device_design_img_id.setter
    def device_design_img_id(self, value):
        self._device_design_img_id = value
    @property
    def device_img(self):
        return self._device_img

    @device_img.setter
    def device_img(self, value):
        self._device_img = value
    @property
    def device_img_id(self):
        return self._device_img_id

    @device_img_id.setter
    def device_img_id(self, value):
        self._device_img_id = value
    @property
    def device_name(self):
        return self._device_name

    @device_name.setter
    def device_name(self, value):
        self._device_name = value
    @property
    def device_other_desc(self):
        return self._device_other_desc

    @device_other_desc.setter
    def device_other_desc(self, value):
        self._device_other_desc = value
    @property
    def face_camera(self):
        return self._face_camera

    @face_camera.setter
    def face_camera(self, value):
        self._face_camera = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def line_network_mode(self):
        return self._line_network_mode

    @line_network_mode.setter
    def line_network_mode(self, value):
        self._line_network_mode = value
    @property
    def line_network_mode_text(self):
        return self._line_network_mode_text

    @line_network_mode_text.setter
    def line_network_mode_text(self, value):
        self._line_network_mode_text = value
    @property
    def memory(self):
        return self._memory

    @memory.setter
    def memory(self, value):
        self._memory = value
    @property
    def min_os_version(self):
        return self._min_os_version

    @min_os_version.setter
    def min_os_version(self, value):
        self._min_os_version = value
    @property
    def model_number(self):
        return self._model_number

    @model_number.setter
    def model_number(self, value):
        self._model_number = value
    @property
    def network_mode(self):
        return self._network_mode

    @network_mode.setter
    def network_mode(self, value):
        self._network_mode = value
    @property
    def network_mode_text(self):
        return self._network_mode_text

    @network_mode_text.setter
    def network_mode_text(self, value):
        self._network_mode_text = value
    @property
    def os_type(self):
        return self._os_type

    @os_type.setter
    def os_type(self, value):
        self._os_type = value
    @property
    def printer(self):
        return self._printer

    @printer.setter
    def printer(self, value):
        self._printer = value
    @property
    def ram(self):
        return self._ram

    @ram.setter
    def ram(self, value):
        self._ram = value
    @property
    def rom(self):
        return self._rom

    @rom.setter
    def rom(self, value):
        self._rom = value
    @property
    def scan_code_mode(self):
        return self._scan_code_mode

    @scan_code_mode.setter
    def scan_code_mode(self, value):
        self._scan_code_mode = value
    @property
    def scan_code_read_dista(self):
        return self._scan_code_read_dista

    @scan_code_read_dista.setter
    def scan_code_read_dista(self, value):
        self._scan_code_read_dista = value
    @property
    def screen_dpi(self):
        return self._screen_dpi

    @screen_dpi.setter
    def screen_dpi(self, value):
        self._screen_dpi = value
    @property
    def screen_size(self):
        return self._screen_size

    @screen_size.setter
    def screen_size(self, value):
        self._screen_size = value
    @property
    def sdk_auto_file(self):
        return self._sdk_auto_file

    @sdk_auto_file.setter
    def sdk_auto_file(self, value):
        self._sdk_auto_file = value
    @property
    def sdk_auto_file_id(self):
        return self._sdk_auto_file_id

    @sdk_auto_file_id.setter
    def sdk_auto_file_id(self, value):
        self._sdk_auto_file_id = value
    @property
    def sdk_name(self):
        return self._sdk_name

    @sdk_name.setter
    def sdk_name(self, value):
        self._sdk_name = value
    @property
    def sdk_version(self):
        return self._sdk_version

    @sdk_version.setter
    def sdk_version(self, value):
        self._sdk_version = value
    @property
    def storage(self):
        return self._storage

    @storage.setter
    def storage(self, value):
        self._storage = value
    @property
    def supplier_name(self):
        return self._supplier_name

    @supplier_name.setter
    def supplier_name(self, value):
        self._supplier_name = value
    @property
    def supplier_pid(self):
        return self._supplier_pid

    @supplier_pid.setter
    def supplier_pid(self, value):
        self._supplier_pid = value
    @property
    def supplier_sn(self):
        return self._supplier_sn

    @supplier_sn.setter
    def supplier_sn(self, value):
        self._supplier_sn = value
    @property
    def tranaction_model(self):
        return self._tranaction_model

    @tranaction_model.setter
    def tranaction_model(self, value):
        self._tranaction_model = value
    @property
    def tranaction_model_text(self):
        return self._tranaction_model_text

    @tranaction_model_text.setter
    def tranaction_model_text(self, value):
        self._tranaction_model_text = value
    @property
    def wifi_mode(self):
        return self._wifi_mode

    @wifi_mode.setter
    def wifi_mode(self, value):
        self._wifi_mode = value
    @property
    def wifi_mode_text(self):
        return self._wifi_mode_text

    @wifi_mode_text.setter
    def wifi_mode_text(self, value):
        self._wifi_mode_text = value


    def to_alipay_dict(self):
        params = dict()
        if self.approval_remark:
            if hasattr(self.approval_remark, 'to_alipay_dict'):
                params['approval_remark'] = self.approval_remark.to_alipay_dict()
            else:
                params['approval_remark'] = self.approval_remark
        if self.approval_status:
            if hasattr(self.approval_status, 'to_alipay_dict'):
                params['approval_status'] = self.approval_status.to_alipay_dict()
            else:
                params['approval_status'] = self.approval_status
        if self.approval_status_text:
            if hasattr(self.approval_status_text, 'to_alipay_dict'):
                params['approval_status_text'] = self.approval_status_text.to_alipay_dict()
            else:
                params['approval_status_text'] = self.approval_status_text
        if self.bluetooth_mode:
            if hasattr(self.bluetooth_mode, 'to_alipay_dict'):
                params['bluetooth_mode'] = self.bluetooth_mode.to_alipay_dict()
            else:
                params['bluetooth_mode'] = self.bluetooth_mode
        if self.bluetooth_mode_text:
            if hasattr(self.bluetooth_mode_text, 'to_alipay_dict'):
                params['bluetooth_mode_text'] = self.bluetooth_mode_text.to_alipay_dict()
            else:
                params['bluetooth_mode_text'] = self.bluetooth_mode_text
        if self.contact_address:
            if hasattr(self.contact_address, 'to_alipay_dict'):
                params['contact_address'] = self.contact_address.to_alipay_dict()
            else:
                params['contact_address'] = self.contact_address
        if self.contact_mobile:
            if hasattr(self.contact_mobile, 'to_alipay_dict'):
                params['contact_mobile'] = self.contact_mobile.to_alipay_dict()
            else:
                params['contact_mobile'] = self.contact_mobile
        if self.contact_name:
            if hasattr(self.contact_name, 'to_alipay_dict'):
                params['contact_name'] = self.contact_name.to_alipay_dict()
            else:
                params['contact_name'] = self.contact_name
        if self.cpu:
            if hasattr(self.cpu, 'to_alipay_dict'):
                params['cpu'] = self.cpu.to_alipay_dict()
            else:
                params['cpu'] = self.cpu
        if self.device_design_img:
            if hasattr(self.device_design_img, 'to_alipay_dict'):
                params['device_design_img'] = self.device_design_img.to_alipay_dict()
            else:
                params['device_design_img'] = self.device_design_img
        if self.device_design_img_id:
            if hasattr(self.device_design_img_id, 'to_alipay_dict'):
                params['device_design_img_id'] = self.device_design_img_id.to_alipay_dict()
            else:
                params['device_design_img_id'] = self.device_design_img_id
        if self.device_img:
            if hasattr(self.device_img, 'to_alipay_dict'):
                params['device_img'] = self.device_img.to_alipay_dict()
            else:
                params['device_img'] = self.device_img
        if self.device_img_id:
            if hasattr(self.device_img_id, 'to_alipay_dict'):
                params['device_img_id'] = self.device_img_id.to_alipay_dict()
            else:
                params['device_img_id'] = self.device_img_id
        if self.device_name:
            if hasattr(self.device_name, 'to_alipay_dict'):
                params['device_name'] = self.device_name.to_alipay_dict()
            else:
                params['device_name'] = self.device_name
        if self.device_other_desc:
            if hasattr(self.device_other_desc, 'to_alipay_dict'):
                params['device_other_desc'] = self.device_other_desc.to_alipay_dict()
            else:
                params['device_other_desc'] = self.device_other_desc
        if self.face_camera:
            if hasattr(self.face_camera, 'to_alipay_dict'):
                params['face_camera'] = self.face_camera.to_alipay_dict()
            else:
                params['face_camera'] = self.face_camera
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.line_network_mode:
            if hasattr(self.line_network_mode, 'to_alipay_dict'):
                params['line_network_mode'] = self.line_network_mode.to_alipay_dict()
            else:
                params['line_network_mode'] = self.line_network_mode
        if self.line_network_mode_text:
            if hasattr(self.line_network_mode_text, 'to_alipay_dict'):
                params['line_network_mode_text'] = self.line_network_mode_text.to_alipay_dict()
            else:
                params['line_network_mode_text'] = self.line_network_mode_text
        if self.memory:
            if hasattr(self.memory, 'to_alipay_dict'):
                params['memory'] = self.memory.to_alipay_dict()
            else:
                params['memory'] = self.memory
        if self.min_os_version:
            if hasattr(self.min_os_version, 'to_alipay_dict'):
                params['min_os_version'] = self.min_os_version.to_alipay_dict()
            else:
                params['min_os_version'] = self.min_os_version
        if self.model_number:
            if hasattr(self.model_number, 'to_alipay_dict'):
                params['model_number'] = self.model_number.to_alipay_dict()
            else:
                params['model_number'] = self.model_number
        if self.network_mode:
            if hasattr(self.network_mode, 'to_alipay_dict'):
                params['network_mode'] = self.network_mode.to_alipay_dict()
            else:
                params['network_mode'] = self.network_mode
        if self.network_mode_text:
            if hasattr(self.network_mode_text, 'to_alipay_dict'):
                params['network_mode_text'] = self.network_mode_text.to_alipay_dict()
            else:
                params['network_mode_text'] = self.network_mode_text
        if self.os_type:
            if hasattr(self.os_type, 'to_alipay_dict'):
                params['os_type'] = self.os_type.to_alipay_dict()
            else:
                params['os_type'] = self.os_type
        if self.printer:
            if hasattr(self.printer, 'to_alipay_dict'):
                params['printer'] = self.printer.to_alipay_dict()
            else:
                params['printer'] = self.printer
        if self.ram:
            if hasattr(self.ram, 'to_alipay_dict'):
                params['ram'] = self.ram.to_alipay_dict()
            else:
                params['ram'] = self.ram
        if self.rom:
            if hasattr(self.rom, 'to_alipay_dict'):
                params['rom'] = self.rom.to_alipay_dict()
            else:
                params['rom'] = self.rom
        if self.scan_code_mode:
            if hasattr(self.scan_code_mode, 'to_alipay_dict'):
                params['scan_code_mode'] = self.scan_code_mode.to_alipay_dict()
            else:
                params['scan_code_mode'] = self.scan_code_mode
        if self.scan_code_read_dista:
            if hasattr(self.scan_code_read_dista, 'to_alipay_dict'):
                params['scan_code_read_dista'] = self.scan_code_read_dista.to_alipay_dict()
            else:
                params['scan_code_read_dista'] = self.scan_code_read_dista
        if self.screen_dpi:
            if hasattr(self.screen_dpi, 'to_alipay_dict'):
                params['screen_dpi'] = self.screen_dpi.to_alipay_dict()
            else:
                params['screen_dpi'] = self.screen_dpi
        if self.screen_size:
            if hasattr(self.screen_size, 'to_alipay_dict'):
                params['screen_size'] = self.screen_size.to_alipay_dict()
            else:
                params['screen_size'] = self.screen_size
        if self.sdk_auto_file:
            if hasattr(self.sdk_auto_file, 'to_alipay_dict'):
                params['sdk_auto_file'] = self.sdk_auto_file.to_alipay_dict()
            else:
                params['sdk_auto_file'] = self.sdk_auto_file
        if self.sdk_auto_file_id:
            if hasattr(self.sdk_auto_file_id, 'to_alipay_dict'):
                params['sdk_auto_file_id'] = self.sdk_auto_file_id.to_alipay_dict()
            else:
                params['sdk_auto_file_id'] = self.sdk_auto_file_id
        if self.sdk_name:
            if hasattr(self.sdk_name, 'to_alipay_dict'):
                params['sdk_name'] = self.sdk_name.to_alipay_dict()
            else:
                params['sdk_name'] = self.sdk_name
        if self.sdk_version:
            if hasattr(self.sdk_version, 'to_alipay_dict'):
                params['sdk_version'] = self.sdk_version.to_alipay_dict()
            else:
                params['sdk_version'] = self.sdk_version
        if self.storage:
            if hasattr(self.storage, 'to_alipay_dict'):
                params['storage'] = self.storage.to_alipay_dict()
            else:
                params['storage'] = self.storage
        if self.supplier_name:
            if hasattr(self.supplier_name, 'to_alipay_dict'):
                params['supplier_name'] = self.supplier_name.to_alipay_dict()
            else:
                params['supplier_name'] = self.supplier_name
        if self.supplier_pid:
            if hasattr(self.supplier_pid, 'to_alipay_dict'):
                params['supplier_pid'] = self.supplier_pid.to_alipay_dict()
            else:
                params['supplier_pid'] = self.supplier_pid
        if self.supplier_sn:
            if hasattr(self.supplier_sn, 'to_alipay_dict'):
                params['supplier_sn'] = self.supplier_sn.to_alipay_dict()
            else:
                params['supplier_sn'] = self.supplier_sn
        if self.tranaction_model:
            if hasattr(self.tranaction_model, 'to_alipay_dict'):
                params['tranaction_model'] = self.tranaction_model.to_alipay_dict()
            else:
                params['tranaction_model'] = self.tranaction_model
        if self.tranaction_model_text:
            if hasattr(self.tranaction_model_text, 'to_alipay_dict'):
                params['tranaction_model_text'] = self.tranaction_model_text.to_alipay_dict()
            else:
                params['tranaction_model_text'] = self.tranaction_model_text
        if self.wifi_mode:
            if hasattr(self.wifi_mode, 'to_alipay_dict'):
                params['wifi_mode'] = self.wifi_mode.to_alipay_dict()
            else:
                params['wifi_mode'] = self.wifi_mode
        if self.wifi_mode_text:
            if hasattr(self.wifi_mode_text, 'to_alipay_dict'):
                params['wifi_mode_text'] = self.wifi_mode_text.to_alipay_dict()
            else:
                params['wifi_mode_text'] = self.wifi_mode_text
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SupplierAssetResponse()
        if 'approval_remark' in d:
            o.approval_remark = d['approval_remark']
        if 'approval_status' in d:
            o.approval_status = d['approval_status']
        if 'approval_status_text' in d:
            o.approval_status_text = d['approval_status_text']
        if 'bluetooth_mode' in d:
            o.bluetooth_mode = d['bluetooth_mode']
        if 'bluetooth_mode_text' in d:
            o.bluetooth_mode_text = d['bluetooth_mode_text']
        if 'contact_address' in d:
            o.contact_address = d['contact_address']
        if 'contact_mobile' in d:
            o.contact_mobile = d['contact_mobile']
        if 'contact_name' in d:
            o.contact_name = d['contact_name']
        if 'cpu' in d:
            o.cpu = d['cpu']
        if 'device_design_img' in d:
            o.device_design_img = d['device_design_img']
        if 'device_design_img_id' in d:
            o.device_design_img_id = d['device_design_img_id']
        if 'device_img' in d:
            o.device_img = d['device_img']
        if 'device_img_id' in d:
            o.device_img_id = d['device_img_id']
        if 'device_name' in d:
            o.device_name = d['device_name']
        if 'device_other_desc' in d:
            o.device_other_desc = d['device_other_desc']
        if 'face_camera' in d:
            o.face_camera = d['face_camera']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'id' in d:
            o.id = d['id']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'line_network_mode' in d:
            o.line_network_mode = d['line_network_mode']
        if 'line_network_mode_text' in d:
            o.line_network_mode_text = d['line_network_mode_text']
        if 'memory' in d:
            o.memory = d['memory']
        if 'min_os_version' in d:
            o.min_os_version = d['min_os_version']
        if 'model_number' in d:
            o.model_number = d['model_number']
        if 'network_mode' in d:
            o.network_mode = d['network_mode']
        if 'network_mode_text' in d:
            o.network_mode_text = d['network_mode_text']
        if 'os_type' in d:
            o.os_type = d['os_type']
        if 'printer' in d:
            o.printer = d['printer']
        if 'ram' in d:
            o.ram = d['ram']
        if 'rom' in d:
            o.rom = d['rom']
        if 'scan_code_mode' in d:
            o.scan_code_mode = d['scan_code_mode']
        if 'scan_code_read_dista' in d:
            o.scan_code_read_dista = d['scan_code_read_dista']
        if 'screen_dpi' in d:
            o.screen_dpi = d['screen_dpi']
        if 'screen_size' in d:
            o.screen_size = d['screen_size']
        if 'sdk_auto_file' in d:
            o.sdk_auto_file = d['sdk_auto_file']
        if 'sdk_auto_file_id' in d:
            o.sdk_auto_file_id = d['sdk_auto_file_id']
        if 'sdk_name' in d:
            o.sdk_name = d['sdk_name']
        if 'sdk_version' in d:
            o.sdk_version = d['sdk_version']
        if 'storage' in d:
            o.storage = d['storage']
        if 'supplier_name' in d:
            o.supplier_name = d['supplier_name']
        if 'supplier_pid' in d:
            o.supplier_pid = d['supplier_pid']
        if 'supplier_sn' in d:
            o.supplier_sn = d['supplier_sn']
        if 'tranaction_model' in d:
            o.tranaction_model = d['tranaction_model']
        if 'tranaction_model_text' in d:
            o.tranaction_model_text = d['tranaction_model_text']
        if 'wifi_mode' in d:
            o.wifi_mode = d['wifi_mode']
        if 'wifi_mode_text' in d:
            o.wifi_mode_text = d['wifi_mode_text']
        return o


