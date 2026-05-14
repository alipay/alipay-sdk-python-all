#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MaterialQueryAttachmentDTO import MaterialQueryAttachmentDTO


class AnttechOceanbaseObglobalMaterialSyncModel(object):

    def __init__(self):
        self._attachment_name = None
        self._attachments = None
        self._certification_unit = None
        self._display_name = None
        self._material_no = None
        self._material_type = None
        self._remark = None
        self._valid_until = None

    @property
    def attachment_name(self):
        return self._attachment_name

    @attachment_name.setter
    def attachment_name(self, value):
        self._attachment_name = value
    @property
    def attachments(self):
        return self._attachments

    @attachments.setter
    def attachments(self, value):
        if isinstance(value, list):
            self._attachments = list()
            for i in value:
                if isinstance(i, MaterialQueryAttachmentDTO):
                    self._attachments.append(i)
                else:
                    self._attachments.append(MaterialQueryAttachmentDTO.from_alipay_dict(i))
    @property
    def certification_unit(self):
        return self._certification_unit

    @certification_unit.setter
    def certification_unit(self, value):
        self._certification_unit = value
    @property
    def display_name(self):
        return self._display_name

    @display_name.setter
    def display_name(self, value):
        self._display_name = value
    @property
    def material_no(self):
        return self._material_no

    @material_no.setter
    def material_no(self, value):
        self._material_no = value
    @property
    def material_type(self):
        return self._material_type

    @material_type.setter
    def material_type(self, value):
        self._material_type = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def valid_until(self):
        return self._valid_until

    @valid_until.setter
    def valid_until(self, value):
        self._valid_until = value


    def to_alipay_dict(self):
        params = dict()
        if self.attachment_name:
            if hasattr(self.attachment_name, 'to_alipay_dict'):
                params['attachment_name'] = self.attachment_name.to_alipay_dict()
            else:
                params['attachment_name'] = self.attachment_name
        if self.attachments:
            if isinstance(self.attachments, list):
                for i in range(0, len(self.attachments)):
                    element = self.attachments[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attachments[i] = element.to_alipay_dict()
            if hasattr(self.attachments, 'to_alipay_dict'):
                params['attachments'] = self.attachments.to_alipay_dict()
            else:
                params['attachments'] = self.attachments
        if self.certification_unit:
            if hasattr(self.certification_unit, 'to_alipay_dict'):
                params['certification_unit'] = self.certification_unit.to_alipay_dict()
            else:
                params['certification_unit'] = self.certification_unit
        if self.display_name:
            if hasattr(self.display_name, 'to_alipay_dict'):
                params['display_name'] = self.display_name.to_alipay_dict()
            else:
                params['display_name'] = self.display_name
        if self.material_no:
            if hasattr(self.material_no, 'to_alipay_dict'):
                params['material_no'] = self.material_no.to_alipay_dict()
            else:
                params['material_no'] = self.material_no
        if self.material_type:
            if hasattr(self.material_type, 'to_alipay_dict'):
                params['material_type'] = self.material_type.to_alipay_dict()
            else:
                params['material_type'] = self.material_type
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.valid_until:
            if hasattr(self.valid_until, 'to_alipay_dict'):
                params['valid_until'] = self.valid_until.to_alipay_dict()
            else:
                params['valid_until'] = self.valid_until
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalMaterialSyncModel()
        if 'attachment_name' in d:
            o.attachment_name = d['attachment_name']
        if 'attachments' in d:
            o.attachments = d['attachments']
        if 'certification_unit' in d:
            o.certification_unit = d['certification_unit']
        if 'display_name' in d:
            o.display_name = d['display_name']
        if 'material_no' in d:
            o.material_no = d['material_no']
        if 'material_type' in d:
            o.material_type = d['material_type']
        if 'remark' in d:
            o.remark = d['remark']
        if 'valid_until' in d:
            o.valid_until = d['valid_until']
        return o


