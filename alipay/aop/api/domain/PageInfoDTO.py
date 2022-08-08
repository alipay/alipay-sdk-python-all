#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OperationTaskDTO import OperationTaskDTO


class PageInfoDTO(object):

    def __init__(self):
        self._code = None
        self._creator_id = None
        self._creator_name = None
        self._current_version = None
        self._edit_version = None
        self._gmt_create = None
        self._gmt_create_code = None
        self._gmt_modified = None
        self._id = None
        self._modifier_id = None
        self._modifier_name = None
        self._name = None
        self._operation_task = None
        self._operation_task_id = None
        self._page_template_type = None
        self._peiqi_status = None
        self._promo_benefit_code = None
        self._reject_reason = None
        self._render_url = None
        self._run_version = None
        self._status = None
        self._template_code = None
        self._template_params = None
        self._tenant_code = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def creator_id(self):
        return self._creator_id

    @creator_id.setter
    def creator_id(self, value):
        self._creator_id = value
    @property
    def creator_name(self):
        return self._creator_name

    @creator_name.setter
    def creator_name(self, value):
        self._creator_name = value
    @property
    def current_version(self):
        return self._current_version

    @current_version.setter
    def current_version(self, value):
        self._current_version = value
    @property
    def edit_version(self):
        return self._edit_version

    @edit_version.setter
    def edit_version(self, value):
        self._edit_version = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_create_code(self):
        return self._gmt_create_code

    @gmt_create_code.setter
    def gmt_create_code(self, value):
        self._gmt_create_code = value
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
    def modifier_id(self):
        return self._modifier_id

    @modifier_id.setter
    def modifier_id(self, value):
        self._modifier_id = value
    @property
    def modifier_name(self):
        return self._modifier_name

    @modifier_name.setter
    def modifier_name(self, value):
        self._modifier_name = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def operation_task(self):
        return self._operation_task

    @operation_task.setter
    def operation_task(self, value):
        if isinstance(value, OperationTaskDTO):
            self._operation_task = value
        else:
            self._operation_task = OperationTaskDTO.from_alipay_dict(value)
    @property
    def operation_task_id(self):
        return self._operation_task_id

    @operation_task_id.setter
    def operation_task_id(self, value):
        self._operation_task_id = value
    @property
    def page_template_type(self):
        return self._page_template_type

    @page_template_type.setter
    def page_template_type(self, value):
        self._page_template_type = value
    @property
    def peiqi_status(self):
        return self._peiqi_status

    @peiqi_status.setter
    def peiqi_status(self, value):
        self._peiqi_status = value
    @property
    def promo_benefit_code(self):
        return self._promo_benefit_code

    @promo_benefit_code.setter
    def promo_benefit_code(self, value):
        self._promo_benefit_code = value
    @property
    def reject_reason(self):
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, value):
        self._reject_reason = value
    @property
    def render_url(self):
        return self._render_url

    @render_url.setter
    def render_url(self, value):
        self._render_url = value
    @property
    def run_version(self):
        return self._run_version

    @run_version.setter
    def run_version(self, value):
        self._run_version = value
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
    def template_params(self):
        return self._template_params

    @template_params.setter
    def template_params(self, value):
        self._template_params = value
    @property
    def tenant_code(self):
        return self._tenant_code

    @tenant_code.setter
    def tenant_code(self, value):
        self._tenant_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.creator_id:
            if hasattr(self.creator_id, 'to_alipay_dict'):
                params['creator_id'] = self.creator_id.to_alipay_dict()
            else:
                params['creator_id'] = self.creator_id
        if self.creator_name:
            if hasattr(self.creator_name, 'to_alipay_dict'):
                params['creator_name'] = self.creator_name.to_alipay_dict()
            else:
                params['creator_name'] = self.creator_name
        if self.current_version:
            if hasattr(self.current_version, 'to_alipay_dict'):
                params['current_version'] = self.current_version.to_alipay_dict()
            else:
                params['current_version'] = self.current_version
        if self.edit_version:
            if hasattr(self.edit_version, 'to_alipay_dict'):
                params['edit_version'] = self.edit_version.to_alipay_dict()
            else:
                params['edit_version'] = self.edit_version
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_create_code:
            if hasattr(self.gmt_create_code, 'to_alipay_dict'):
                params['gmt_create_code'] = self.gmt_create_code.to_alipay_dict()
            else:
                params['gmt_create_code'] = self.gmt_create_code
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
        if self.modifier_id:
            if hasattr(self.modifier_id, 'to_alipay_dict'):
                params['modifier_id'] = self.modifier_id.to_alipay_dict()
            else:
                params['modifier_id'] = self.modifier_id
        if self.modifier_name:
            if hasattr(self.modifier_name, 'to_alipay_dict'):
                params['modifier_name'] = self.modifier_name.to_alipay_dict()
            else:
                params['modifier_name'] = self.modifier_name
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.operation_task:
            if hasattr(self.operation_task, 'to_alipay_dict'):
                params['operation_task'] = self.operation_task.to_alipay_dict()
            else:
                params['operation_task'] = self.operation_task
        if self.operation_task_id:
            if hasattr(self.operation_task_id, 'to_alipay_dict'):
                params['operation_task_id'] = self.operation_task_id.to_alipay_dict()
            else:
                params['operation_task_id'] = self.operation_task_id
        if self.page_template_type:
            if hasattr(self.page_template_type, 'to_alipay_dict'):
                params['page_template_type'] = self.page_template_type.to_alipay_dict()
            else:
                params['page_template_type'] = self.page_template_type
        if self.peiqi_status:
            if hasattr(self.peiqi_status, 'to_alipay_dict'):
                params['peiqi_status'] = self.peiqi_status.to_alipay_dict()
            else:
                params['peiqi_status'] = self.peiqi_status
        if self.promo_benefit_code:
            if hasattr(self.promo_benefit_code, 'to_alipay_dict'):
                params['promo_benefit_code'] = self.promo_benefit_code.to_alipay_dict()
            else:
                params['promo_benefit_code'] = self.promo_benefit_code
        if self.reject_reason:
            if hasattr(self.reject_reason, 'to_alipay_dict'):
                params['reject_reason'] = self.reject_reason.to_alipay_dict()
            else:
                params['reject_reason'] = self.reject_reason
        if self.render_url:
            if hasattr(self.render_url, 'to_alipay_dict'):
                params['render_url'] = self.render_url.to_alipay_dict()
            else:
                params['render_url'] = self.render_url
        if self.run_version:
            if hasattr(self.run_version, 'to_alipay_dict'):
                params['run_version'] = self.run_version.to_alipay_dict()
            else:
                params['run_version'] = self.run_version
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
        if self.template_params:
            if hasattr(self.template_params, 'to_alipay_dict'):
                params['template_params'] = self.template_params.to_alipay_dict()
            else:
                params['template_params'] = self.template_params
        if self.tenant_code:
            if hasattr(self.tenant_code, 'to_alipay_dict'):
                params['tenant_code'] = self.tenant_code.to_alipay_dict()
            else:
                params['tenant_code'] = self.tenant_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PageInfoDTO()
        if 'code' in d:
            o.code = d['code']
        if 'creator_id' in d:
            o.creator_id = d['creator_id']
        if 'creator_name' in d:
            o.creator_name = d['creator_name']
        if 'current_version' in d:
            o.current_version = d['current_version']
        if 'edit_version' in d:
            o.edit_version = d['edit_version']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_create_code' in d:
            o.gmt_create_code = d['gmt_create_code']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'id' in d:
            o.id = d['id']
        if 'modifier_id' in d:
            o.modifier_id = d['modifier_id']
        if 'modifier_name' in d:
            o.modifier_name = d['modifier_name']
        if 'name' in d:
            o.name = d['name']
        if 'operation_task' in d:
            o.operation_task = d['operation_task']
        if 'operation_task_id' in d:
            o.operation_task_id = d['operation_task_id']
        if 'page_template_type' in d:
            o.page_template_type = d['page_template_type']
        if 'peiqi_status' in d:
            o.peiqi_status = d['peiqi_status']
        if 'promo_benefit_code' in d:
            o.promo_benefit_code = d['promo_benefit_code']
        if 'reject_reason' in d:
            o.reject_reason = d['reject_reason']
        if 'render_url' in d:
            o.render_url = d['render_url']
        if 'run_version' in d:
            o.run_version = d['run_version']
        if 'status' in d:
            o.status = d['status']
        if 'template_code' in d:
            o.template_code = d['template_code']
        if 'template_params' in d:
            o.template_params = d['template_params']
        if 'tenant_code' in d:
            o.tenant_code = d['tenant_code']
        return o


