#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BccEventDetail import BccEventDetail
from alipay.aop.api.domain.BccSubjectDetail import BccSubjectDetail


class ZmContractDetail(object):

    def __init__(self):
        self._cancel_operator = None
        self._cancel_supported = None
        self._contract_content = None
        self._contract_no = None
        self._contract_principal_desc = None
        self._contract_principal_logo = None
        self._contract_status = None
        self._event_detail = None
        self._ext_info = None
        self._fufilment_callback_url = None
        self._fufilment_cnt = None
        self._fufilment_desc = None
        self._fufilment_end_time = None
        self._fufilment_period_type = None
        self._fufilment_start_time = None
        self._gmt_accept = None
        self._gmt_cancel = None
        self._gmt_due = None
        self._gmt_end = None
        self._gmt_valid = None
        self._item_end_time = None
        self._item_no = None
        self._item_start_time = None
        self._offer_creater_id = None
        self._offer_creater_name = None
        self._offer_creater_type = None
        self._offer_no = None
        self._out_biz_no = None
        self._out_content_no = None
        self._sign_principal_id = None
        self._sign_principal_type = None
        self._subjects = None

    @property
    def cancel_operator(self):
        return self._cancel_operator

    @cancel_operator.setter
    def cancel_operator(self, value):
        self._cancel_operator = value
    @property
    def cancel_supported(self):
        return self._cancel_supported

    @cancel_supported.setter
    def cancel_supported(self, value):
        self._cancel_supported = value
    @property
    def contract_content(self):
        return self._contract_content

    @contract_content.setter
    def contract_content(self, value):
        self._contract_content = value
    @property
    def contract_no(self):
        return self._contract_no

    @contract_no.setter
    def contract_no(self, value):
        self._contract_no = value
    @property
    def contract_principal_desc(self):
        return self._contract_principal_desc

    @contract_principal_desc.setter
    def contract_principal_desc(self, value):
        self._contract_principal_desc = value
    @property
    def contract_principal_logo(self):
        return self._contract_principal_logo

    @contract_principal_logo.setter
    def contract_principal_logo(self, value):
        self._contract_principal_logo = value
    @property
    def contract_status(self):
        return self._contract_status

    @contract_status.setter
    def contract_status(self, value):
        self._contract_status = value
    @property
    def event_detail(self):
        return self._event_detail

    @event_detail.setter
    def event_detail(self, value):
        if isinstance(value, list):
            self._event_detail = list()
            for i in value:
                if isinstance(i, BccEventDetail):
                    self._event_detail.append(i)
                else:
                    self._event_detail.append(BccEventDetail.from_alipay_dict(i))
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def fufilment_callback_url(self):
        return self._fufilment_callback_url

    @fufilment_callback_url.setter
    def fufilment_callback_url(self, value):
        self._fufilment_callback_url = value
    @property
    def fufilment_cnt(self):
        return self._fufilment_cnt

    @fufilment_cnt.setter
    def fufilment_cnt(self, value):
        self._fufilment_cnt = value
    @property
    def fufilment_desc(self):
        return self._fufilment_desc

    @fufilment_desc.setter
    def fufilment_desc(self, value):
        self._fufilment_desc = value
    @property
    def fufilment_end_time(self):
        return self._fufilment_end_time

    @fufilment_end_time.setter
    def fufilment_end_time(self, value):
        self._fufilment_end_time = value
    @property
    def fufilment_period_type(self):
        return self._fufilment_period_type

    @fufilment_period_type.setter
    def fufilment_period_type(self, value):
        self._fufilment_period_type = value
    @property
    def fufilment_start_time(self):
        return self._fufilment_start_time

    @fufilment_start_time.setter
    def fufilment_start_time(self, value):
        self._fufilment_start_time = value
    @property
    def gmt_accept(self):
        return self._gmt_accept

    @gmt_accept.setter
    def gmt_accept(self, value):
        self._gmt_accept = value
    @property
    def gmt_cancel(self):
        return self._gmt_cancel

    @gmt_cancel.setter
    def gmt_cancel(self, value):
        self._gmt_cancel = value
    @property
    def gmt_due(self):
        return self._gmt_due

    @gmt_due.setter
    def gmt_due(self, value):
        self._gmt_due = value
    @property
    def gmt_end(self):
        return self._gmt_end

    @gmt_end.setter
    def gmt_end(self, value):
        self._gmt_end = value
    @property
    def gmt_valid(self):
        return self._gmt_valid

    @gmt_valid.setter
    def gmt_valid(self, value):
        self._gmt_valid = value
    @property
    def item_end_time(self):
        return self._item_end_time

    @item_end_time.setter
    def item_end_time(self, value):
        self._item_end_time = value
    @property
    def item_no(self):
        return self._item_no

    @item_no.setter
    def item_no(self, value):
        self._item_no = value
    @property
    def item_start_time(self):
        return self._item_start_time

    @item_start_time.setter
    def item_start_time(self, value):
        self._item_start_time = value
    @property
    def offer_creater_id(self):
        return self._offer_creater_id

    @offer_creater_id.setter
    def offer_creater_id(self, value):
        self._offer_creater_id = value
    @property
    def offer_creater_name(self):
        return self._offer_creater_name

    @offer_creater_name.setter
    def offer_creater_name(self, value):
        self._offer_creater_name = value
    @property
    def offer_creater_type(self):
        return self._offer_creater_type

    @offer_creater_type.setter
    def offer_creater_type(self, value):
        self._offer_creater_type = value
    @property
    def offer_no(self):
        return self._offer_no

    @offer_no.setter
    def offer_no(self, value):
        self._offer_no = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_content_no(self):
        return self._out_content_no

    @out_content_no.setter
    def out_content_no(self, value):
        self._out_content_no = value
    @property
    def sign_principal_id(self):
        return self._sign_principal_id

    @sign_principal_id.setter
    def sign_principal_id(self, value):
        self._sign_principal_id = value
    @property
    def sign_principal_type(self):
        return self._sign_principal_type

    @sign_principal_type.setter
    def sign_principal_type(self, value):
        self._sign_principal_type = value
    @property
    def subjects(self):
        return self._subjects

    @subjects.setter
    def subjects(self, value):
        if isinstance(value, list):
            self._subjects = list()
            for i in value:
                if isinstance(i, BccSubjectDetail):
                    self._subjects.append(i)
                else:
                    self._subjects.append(BccSubjectDetail.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.cancel_operator:
            if hasattr(self.cancel_operator, 'to_alipay_dict'):
                params['cancel_operator'] = self.cancel_operator.to_alipay_dict()
            else:
                params['cancel_operator'] = self.cancel_operator
        if self.cancel_supported:
            if hasattr(self.cancel_supported, 'to_alipay_dict'):
                params['cancel_supported'] = self.cancel_supported.to_alipay_dict()
            else:
                params['cancel_supported'] = self.cancel_supported
        if self.contract_content:
            if hasattr(self.contract_content, 'to_alipay_dict'):
                params['contract_content'] = self.contract_content.to_alipay_dict()
            else:
                params['contract_content'] = self.contract_content
        if self.contract_no:
            if hasattr(self.contract_no, 'to_alipay_dict'):
                params['contract_no'] = self.contract_no.to_alipay_dict()
            else:
                params['contract_no'] = self.contract_no
        if self.contract_principal_desc:
            if hasattr(self.contract_principal_desc, 'to_alipay_dict'):
                params['contract_principal_desc'] = self.contract_principal_desc.to_alipay_dict()
            else:
                params['contract_principal_desc'] = self.contract_principal_desc
        if self.contract_principal_logo:
            if hasattr(self.contract_principal_logo, 'to_alipay_dict'):
                params['contract_principal_logo'] = self.contract_principal_logo.to_alipay_dict()
            else:
                params['contract_principal_logo'] = self.contract_principal_logo
        if self.contract_status:
            if hasattr(self.contract_status, 'to_alipay_dict'):
                params['contract_status'] = self.contract_status.to_alipay_dict()
            else:
                params['contract_status'] = self.contract_status
        if self.event_detail:
            if isinstance(self.event_detail, list):
                for i in range(0, len(self.event_detail)):
                    element = self.event_detail[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.event_detail[i] = element.to_alipay_dict()
            if hasattr(self.event_detail, 'to_alipay_dict'):
                params['event_detail'] = self.event_detail.to_alipay_dict()
            else:
                params['event_detail'] = self.event_detail
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.fufilment_callback_url:
            if hasattr(self.fufilment_callback_url, 'to_alipay_dict'):
                params['fufilment_callback_url'] = self.fufilment_callback_url.to_alipay_dict()
            else:
                params['fufilment_callback_url'] = self.fufilment_callback_url
        if self.fufilment_cnt:
            if hasattr(self.fufilment_cnt, 'to_alipay_dict'):
                params['fufilment_cnt'] = self.fufilment_cnt.to_alipay_dict()
            else:
                params['fufilment_cnt'] = self.fufilment_cnt
        if self.fufilment_desc:
            if hasattr(self.fufilment_desc, 'to_alipay_dict'):
                params['fufilment_desc'] = self.fufilment_desc.to_alipay_dict()
            else:
                params['fufilment_desc'] = self.fufilment_desc
        if self.fufilment_end_time:
            if hasattr(self.fufilment_end_time, 'to_alipay_dict'):
                params['fufilment_end_time'] = self.fufilment_end_time.to_alipay_dict()
            else:
                params['fufilment_end_time'] = self.fufilment_end_time
        if self.fufilment_period_type:
            if hasattr(self.fufilment_period_type, 'to_alipay_dict'):
                params['fufilment_period_type'] = self.fufilment_period_type.to_alipay_dict()
            else:
                params['fufilment_period_type'] = self.fufilment_period_type
        if self.fufilment_start_time:
            if hasattr(self.fufilment_start_time, 'to_alipay_dict'):
                params['fufilment_start_time'] = self.fufilment_start_time.to_alipay_dict()
            else:
                params['fufilment_start_time'] = self.fufilment_start_time
        if self.gmt_accept:
            if hasattr(self.gmt_accept, 'to_alipay_dict'):
                params['gmt_accept'] = self.gmt_accept.to_alipay_dict()
            else:
                params['gmt_accept'] = self.gmt_accept
        if self.gmt_cancel:
            if hasattr(self.gmt_cancel, 'to_alipay_dict'):
                params['gmt_cancel'] = self.gmt_cancel.to_alipay_dict()
            else:
                params['gmt_cancel'] = self.gmt_cancel
        if self.gmt_due:
            if hasattr(self.gmt_due, 'to_alipay_dict'):
                params['gmt_due'] = self.gmt_due.to_alipay_dict()
            else:
                params['gmt_due'] = self.gmt_due
        if self.gmt_end:
            if hasattr(self.gmt_end, 'to_alipay_dict'):
                params['gmt_end'] = self.gmt_end.to_alipay_dict()
            else:
                params['gmt_end'] = self.gmt_end
        if self.gmt_valid:
            if hasattr(self.gmt_valid, 'to_alipay_dict'):
                params['gmt_valid'] = self.gmt_valid.to_alipay_dict()
            else:
                params['gmt_valid'] = self.gmt_valid
        if self.item_end_time:
            if hasattr(self.item_end_time, 'to_alipay_dict'):
                params['item_end_time'] = self.item_end_time.to_alipay_dict()
            else:
                params['item_end_time'] = self.item_end_time
        if self.item_no:
            if hasattr(self.item_no, 'to_alipay_dict'):
                params['item_no'] = self.item_no.to_alipay_dict()
            else:
                params['item_no'] = self.item_no
        if self.item_start_time:
            if hasattr(self.item_start_time, 'to_alipay_dict'):
                params['item_start_time'] = self.item_start_time.to_alipay_dict()
            else:
                params['item_start_time'] = self.item_start_time
        if self.offer_creater_id:
            if hasattr(self.offer_creater_id, 'to_alipay_dict'):
                params['offer_creater_id'] = self.offer_creater_id.to_alipay_dict()
            else:
                params['offer_creater_id'] = self.offer_creater_id
        if self.offer_creater_name:
            if hasattr(self.offer_creater_name, 'to_alipay_dict'):
                params['offer_creater_name'] = self.offer_creater_name.to_alipay_dict()
            else:
                params['offer_creater_name'] = self.offer_creater_name
        if self.offer_creater_type:
            if hasattr(self.offer_creater_type, 'to_alipay_dict'):
                params['offer_creater_type'] = self.offer_creater_type.to_alipay_dict()
            else:
                params['offer_creater_type'] = self.offer_creater_type
        if self.offer_no:
            if hasattr(self.offer_no, 'to_alipay_dict'):
                params['offer_no'] = self.offer_no.to_alipay_dict()
            else:
                params['offer_no'] = self.offer_no
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.out_content_no:
            if hasattr(self.out_content_no, 'to_alipay_dict'):
                params['out_content_no'] = self.out_content_no.to_alipay_dict()
            else:
                params['out_content_no'] = self.out_content_no
        if self.sign_principal_id:
            if hasattr(self.sign_principal_id, 'to_alipay_dict'):
                params['sign_principal_id'] = self.sign_principal_id.to_alipay_dict()
            else:
                params['sign_principal_id'] = self.sign_principal_id
        if self.sign_principal_type:
            if hasattr(self.sign_principal_type, 'to_alipay_dict'):
                params['sign_principal_type'] = self.sign_principal_type.to_alipay_dict()
            else:
                params['sign_principal_type'] = self.sign_principal_type
        if self.subjects:
            if isinstance(self.subjects, list):
                for i in range(0, len(self.subjects)):
                    element = self.subjects[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.subjects[i] = element.to_alipay_dict()
            if hasattr(self.subjects, 'to_alipay_dict'):
                params['subjects'] = self.subjects.to_alipay_dict()
            else:
                params['subjects'] = self.subjects
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZmContractDetail()
        if 'cancel_operator' in d:
            o.cancel_operator = d['cancel_operator']
        if 'cancel_supported' in d:
            o.cancel_supported = d['cancel_supported']
        if 'contract_content' in d:
            o.contract_content = d['contract_content']
        if 'contract_no' in d:
            o.contract_no = d['contract_no']
        if 'contract_principal_desc' in d:
            o.contract_principal_desc = d['contract_principal_desc']
        if 'contract_principal_logo' in d:
            o.contract_principal_logo = d['contract_principal_logo']
        if 'contract_status' in d:
            o.contract_status = d['contract_status']
        if 'event_detail' in d:
            o.event_detail = d['event_detail']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'fufilment_callback_url' in d:
            o.fufilment_callback_url = d['fufilment_callback_url']
        if 'fufilment_cnt' in d:
            o.fufilment_cnt = d['fufilment_cnt']
        if 'fufilment_desc' in d:
            o.fufilment_desc = d['fufilment_desc']
        if 'fufilment_end_time' in d:
            o.fufilment_end_time = d['fufilment_end_time']
        if 'fufilment_period_type' in d:
            o.fufilment_period_type = d['fufilment_period_type']
        if 'fufilment_start_time' in d:
            o.fufilment_start_time = d['fufilment_start_time']
        if 'gmt_accept' in d:
            o.gmt_accept = d['gmt_accept']
        if 'gmt_cancel' in d:
            o.gmt_cancel = d['gmt_cancel']
        if 'gmt_due' in d:
            o.gmt_due = d['gmt_due']
        if 'gmt_end' in d:
            o.gmt_end = d['gmt_end']
        if 'gmt_valid' in d:
            o.gmt_valid = d['gmt_valid']
        if 'item_end_time' in d:
            o.item_end_time = d['item_end_time']
        if 'item_no' in d:
            o.item_no = d['item_no']
        if 'item_start_time' in d:
            o.item_start_time = d['item_start_time']
        if 'offer_creater_id' in d:
            o.offer_creater_id = d['offer_creater_id']
        if 'offer_creater_name' in d:
            o.offer_creater_name = d['offer_creater_name']
        if 'offer_creater_type' in d:
            o.offer_creater_type = d['offer_creater_type']
        if 'offer_no' in d:
            o.offer_no = d['offer_no']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'out_content_no' in d:
            o.out_content_no = d['out_content_no']
        if 'sign_principal_id' in d:
            o.sign_principal_id = d['sign_principal_id']
        if 'sign_principal_type' in d:
            o.sign_principal_type = d['sign_principal_type']
        if 'subjects' in d:
            o.subjects = d['subjects']
        return o


