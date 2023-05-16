#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ComponentDTO(object):

    def __init__(self):
        self._enable_edit = None
        self._exp = None
        self._exp_return_type = None
        self._id = None
        self._name = None
        self._placeholder = None
        self._readonly = None
        self._ref = None
        self._required = None
        self._size = None
        self._src_content = None
        self._type = None
        self._uk = None
        self._value = None
        self._version_no = None

    @property
    def enable_edit(self):
        return self._enable_edit

    @enable_edit.setter
    def enable_edit(self, value):
        self._enable_edit = value
    @property
    def exp(self):
        return self._exp

    @exp.setter
    def exp(self, value):
        self._exp = value
    @property
    def exp_return_type(self):
        return self._exp_return_type

    @exp_return_type.setter
    def exp_return_type(self, value):
        self._exp_return_type = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def placeholder(self):
        return self._placeholder

    @placeholder.setter
    def placeholder(self, value):
        self._placeholder = value
    @property
    def readonly(self):
        return self._readonly

    @readonly.setter
    def readonly(self, value):
        self._readonly = value
    @property
    def ref(self):
        return self._ref

    @ref.setter
    def ref(self, value):
        self._ref = value
    @property
    def required(self):
        return self._required

    @required.setter
    def required(self, value):
        self._required = value
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value
    @property
    def src_content(self):
        return self._src_content

    @src_content.setter
    def src_content(self, value):
        self._src_content = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def uk(self):
        return self._uk

    @uk.setter
    def uk(self, value):
        self._uk = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
    @property
    def version_no(self):
        return self._version_no

    @version_no.setter
    def version_no(self, value):
        self._version_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.enable_edit:
            if hasattr(self.enable_edit, 'to_alipay_dict'):
                params['enable_edit'] = self.enable_edit.to_alipay_dict()
            else:
                params['enable_edit'] = self.enable_edit
        if self.exp:
            if hasattr(self.exp, 'to_alipay_dict'):
                params['exp'] = self.exp.to_alipay_dict()
            else:
                params['exp'] = self.exp
        if self.exp_return_type:
            if hasattr(self.exp_return_type, 'to_alipay_dict'):
                params['exp_return_type'] = self.exp_return_type.to_alipay_dict()
            else:
                params['exp_return_type'] = self.exp_return_type
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.placeholder:
            if hasattr(self.placeholder, 'to_alipay_dict'):
                params['placeholder'] = self.placeholder.to_alipay_dict()
            else:
                params['placeholder'] = self.placeholder
        if self.readonly:
            if hasattr(self.readonly, 'to_alipay_dict'):
                params['readonly'] = self.readonly.to_alipay_dict()
            else:
                params['readonly'] = self.readonly
        if self.ref:
            if hasattr(self.ref, 'to_alipay_dict'):
                params['ref'] = self.ref.to_alipay_dict()
            else:
                params['ref'] = self.ref
        if self.required:
            if hasattr(self.required, 'to_alipay_dict'):
                params['required'] = self.required.to_alipay_dict()
            else:
                params['required'] = self.required
        if self.size:
            if hasattr(self.size, 'to_alipay_dict'):
                params['size'] = self.size.to_alipay_dict()
            else:
                params['size'] = self.size
        if self.src_content:
            if hasattr(self.src_content, 'to_alipay_dict'):
                params['src_content'] = self.src_content.to_alipay_dict()
            else:
                params['src_content'] = self.src_content
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.uk:
            if hasattr(self.uk, 'to_alipay_dict'):
                params['uk'] = self.uk.to_alipay_dict()
            else:
                params['uk'] = self.uk
        if self.value:
            if hasattr(self.value, 'to_alipay_dict'):
                params['value'] = self.value.to_alipay_dict()
            else:
                params['value'] = self.value
        if self.version_no:
            if hasattr(self.version_no, 'to_alipay_dict'):
                params['version_no'] = self.version_no.to_alipay_dict()
            else:
                params['version_no'] = self.version_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ComponentDTO()
        if 'enable_edit' in d:
            o.enable_edit = d['enable_edit']
        if 'exp' in d:
            o.exp = d['exp']
        if 'exp_return_type' in d:
            o.exp_return_type = d['exp_return_type']
        if 'id' in d:
            o.id = d['id']
        if 'name' in d:
            o.name = d['name']
        if 'placeholder' in d:
            o.placeholder = d['placeholder']
        if 'readonly' in d:
            o.readonly = d['readonly']
        if 'ref' in d:
            o.ref = d['ref']
        if 'required' in d:
            o.required = d['required']
        if 'size' in d:
            o.size = d['size']
        if 'src_content' in d:
            o.src_content = d['src_content']
        if 'type' in d:
            o.type = d['type']
        if 'uk' in d:
            o.uk = d['uk']
        if 'value' in d:
            o.value = d['value']
        if 'version_no' in d:
            o.version_no = d['version_no']
        return o


