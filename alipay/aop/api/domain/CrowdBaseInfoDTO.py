#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FileInfoDTO import FileInfoDTO


class CrowdBaseInfoDTO(object):

    def __init__(self):
        self._crowd_name = None
        self._file_info_dto = None
        self._scene_code = None
        self._source_type = None

    @property
    def crowd_name(self):
        return self._crowd_name

    @crowd_name.setter
    def crowd_name(self, value):
        self._crowd_name = value
    @property
    def file_info_dto(self):
        return self._file_info_dto

    @file_info_dto.setter
    def file_info_dto(self, value):
        if isinstance(value, FileInfoDTO):
            self._file_info_dto = value
        else:
            self._file_info_dto = FileInfoDTO.from_alipay_dict(value)
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def source_type(self):
        return self._source_type

    @source_type.setter
    def source_type(self, value):
        self._source_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.crowd_name:
            if hasattr(self.crowd_name, 'to_alipay_dict'):
                params['crowd_name'] = self.crowd_name.to_alipay_dict()
            else:
                params['crowd_name'] = self.crowd_name
        if self.file_info_dto:
            if hasattr(self.file_info_dto, 'to_alipay_dict'):
                params['file_info_dto'] = self.file_info_dto.to_alipay_dict()
            else:
                params['file_info_dto'] = self.file_info_dto
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.source_type:
            if hasattr(self.source_type, 'to_alipay_dict'):
                params['source_type'] = self.source_type.to_alipay_dict()
            else:
                params['source_type'] = self.source_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CrowdBaseInfoDTO()
        if 'crowd_name' in d:
            o.crowd_name = d['crowd_name']
        if 'file_info_dto' in d:
            o.file_info_dto = d['file_info_dto']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'source_type' in d:
            o.source_type = d['source_type']
        return o


