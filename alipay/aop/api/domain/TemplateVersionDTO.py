#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TemplateVersionDTO(object):

    def __init__(self):
        self._approve_url = None
        self._description = None
        self._edit_address = None
        self._file_address = None
        self._file_name = None
        self._gmt_create = None
        self._gmt_modified = None
        self._html_file_address = None
        self._id = None
        self._pdf_address = None
        self._pdf_presigned_url = None
        self._preview_address = None
        self._preview_presigned_url = None
        self._publish_time = None
        self._status = None
        self._template_code = None
        self._template_lib_code = None
        self._template_name = None
        self._version_no = None
        self._voucher_id = None

    @property
    def approve_url(self):
        return self._approve_url

    @approve_url.setter
    def approve_url(self, value):
        self._approve_url = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def edit_address(self):
        return self._edit_address

    @edit_address.setter
    def edit_address(self, value):
        self._edit_address = value
    @property
    def file_address(self):
        return self._file_address

    @file_address.setter
    def file_address(self, value):
        self._file_address = value
    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value
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
    def html_file_address(self):
        return self._html_file_address

    @html_file_address.setter
    def html_file_address(self, value):
        self._html_file_address = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def pdf_address(self):
        return self._pdf_address

    @pdf_address.setter
    def pdf_address(self, value):
        self._pdf_address = value
    @property
    def pdf_presigned_url(self):
        return self._pdf_presigned_url

    @pdf_presigned_url.setter
    def pdf_presigned_url(self, value):
        self._pdf_presigned_url = value
    @property
    def preview_address(self):
        return self._preview_address

    @preview_address.setter
    def preview_address(self, value):
        self._preview_address = value
    @property
    def preview_presigned_url(self):
        return self._preview_presigned_url

    @preview_presigned_url.setter
    def preview_presigned_url(self, value):
        self._preview_presigned_url = value
    @property
    def publish_time(self):
        return self._publish_time

    @publish_time.setter
    def publish_time(self, value):
        self._publish_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def template_code(self):
        return self._template_code

    @template_code.setter
    def template_code(self, value):
        self._template_code = value
    @property
    def template_lib_code(self):
        return self._template_lib_code

    @template_lib_code.setter
    def template_lib_code(self, value):
        self._template_lib_code = value
    @property
    def template_name(self):
        return self._template_name

    @template_name.setter
    def template_name(self, value):
        self._template_name = value
    @property
    def version_no(self):
        return self._version_no

    @version_no.setter
    def version_no(self, value):
        self._version_no = value
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.approve_url:
            if hasattr(self.approve_url, 'to_alipay_dict'):
                params['approve_url'] = self.approve_url.to_alipay_dict()
            else:
                params['approve_url'] = self.approve_url
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.edit_address:
            if hasattr(self.edit_address, 'to_alipay_dict'):
                params['edit_address'] = self.edit_address.to_alipay_dict()
            else:
                params['edit_address'] = self.edit_address
        if self.file_address:
            if hasattr(self.file_address, 'to_alipay_dict'):
                params['file_address'] = self.file_address.to_alipay_dict()
            else:
                params['file_address'] = self.file_address
        if self.file_name:
            if hasattr(self.file_name, 'to_alipay_dict'):
                params['file_name'] = self.file_name.to_alipay_dict()
            else:
                params['file_name'] = self.file_name
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
        if self.html_file_address:
            if hasattr(self.html_file_address, 'to_alipay_dict'):
                params['html_file_address'] = self.html_file_address.to_alipay_dict()
            else:
                params['html_file_address'] = self.html_file_address
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.pdf_address:
            if hasattr(self.pdf_address, 'to_alipay_dict'):
                params['pdf_address'] = self.pdf_address.to_alipay_dict()
            else:
                params['pdf_address'] = self.pdf_address
        if self.pdf_presigned_url:
            if hasattr(self.pdf_presigned_url, 'to_alipay_dict'):
                params['pdf_presigned_url'] = self.pdf_presigned_url.to_alipay_dict()
            else:
                params['pdf_presigned_url'] = self.pdf_presigned_url
        if self.preview_address:
            if hasattr(self.preview_address, 'to_alipay_dict'):
                params['preview_address'] = self.preview_address.to_alipay_dict()
            else:
                params['preview_address'] = self.preview_address
        if self.preview_presigned_url:
            if hasattr(self.preview_presigned_url, 'to_alipay_dict'):
                params['preview_presigned_url'] = self.preview_presigned_url.to_alipay_dict()
            else:
                params['preview_presigned_url'] = self.preview_presigned_url
        if self.publish_time:
            if hasattr(self.publish_time, 'to_alipay_dict'):
                params['publish_time'] = self.publish_time.to_alipay_dict()
            else:
                params['publish_time'] = self.publish_time
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.template_code:
            if hasattr(self.template_code, 'to_alipay_dict'):
                params['template_code'] = self.template_code.to_alipay_dict()
            else:
                params['template_code'] = self.template_code
        if self.template_lib_code:
            if hasattr(self.template_lib_code, 'to_alipay_dict'):
                params['template_lib_code'] = self.template_lib_code.to_alipay_dict()
            else:
                params['template_lib_code'] = self.template_lib_code
        if self.template_name:
            if hasattr(self.template_name, 'to_alipay_dict'):
                params['template_name'] = self.template_name.to_alipay_dict()
            else:
                params['template_name'] = self.template_name
        if self.version_no:
            if hasattr(self.version_no, 'to_alipay_dict'):
                params['version_no'] = self.version_no.to_alipay_dict()
            else:
                params['version_no'] = self.version_no
        if self.voucher_id:
            if hasattr(self.voucher_id, 'to_alipay_dict'):
                params['voucher_id'] = self.voucher_id.to_alipay_dict()
            else:
                params['voucher_id'] = self.voucher_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TemplateVersionDTO()
        if 'approve_url' in d:
            o.approve_url = d['approve_url']
        if 'description' in d:
            o.description = d['description']
        if 'edit_address' in d:
            o.edit_address = d['edit_address']
        if 'file_address' in d:
            o.file_address = d['file_address']
        if 'file_name' in d:
            o.file_name = d['file_name']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'html_file_address' in d:
            o.html_file_address = d['html_file_address']
        if 'id' in d:
            o.id = d['id']
        if 'pdf_address' in d:
            o.pdf_address = d['pdf_address']
        if 'pdf_presigned_url' in d:
            o.pdf_presigned_url = d['pdf_presigned_url']
        if 'preview_address' in d:
            o.preview_address = d['preview_address']
        if 'preview_presigned_url' in d:
            o.preview_presigned_url = d['preview_presigned_url']
        if 'publish_time' in d:
            o.publish_time = d['publish_time']
        if 'status' in d:
            o.status = d['status']
        if 'template_code' in d:
            o.template_code = d['template_code']
        if 'template_lib_code' in d:
            o.template_lib_code = d['template_lib_code']
        if 'template_name' in d:
            o.template_name = d['template_name']
        if 'version_no' in d:
            o.version_no = d['version_no']
        if 'voucher_id' in d:
            o.voucher_id = d['voucher_id']
        return o


