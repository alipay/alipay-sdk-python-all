#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.WorkDetail import WorkDetail


class KoubeiRetailWmsWorkQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiRetailWmsWorkQueryResponse, self).__init__()
        self._ext_info = None
        self._gmt_finished = None
        self._notice_out_biz_no = None
        self._notice_out_biz_type = None
        self._operator = None
        self._out_biz_no = None
        self._remark = None
        self._status = None
        self._warehouse_code = None
        self._work_details = None
        self._work_id = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def gmt_finished(self):
        return self._gmt_finished

    @gmt_finished.setter
    def gmt_finished(self, value):
        self._gmt_finished = value
    @property
    def notice_out_biz_no(self):
        return self._notice_out_biz_no

    @notice_out_biz_no.setter
    def notice_out_biz_no(self, value):
        self._notice_out_biz_no = value
    @property
    def notice_out_biz_type(self):
        return self._notice_out_biz_type

    @notice_out_biz_type.setter
    def notice_out_biz_type(self, value):
        self._notice_out_biz_type = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def warehouse_code(self):
        return self._warehouse_code

    @warehouse_code.setter
    def warehouse_code(self, value):
        self._warehouse_code = value
    @property
    def work_details(self):
        return self._work_details

    @work_details.setter
    def work_details(self, value):
        if isinstance(value, list):
            self._work_details = list()
            for i in value:
                if isinstance(i, WorkDetail):
                    self._work_details.append(i)
                else:
                    self._work_details.append(WorkDetail.from_alipay_dict(i))
    @property
    def work_id(self):
        return self._work_id

    @work_id.setter
    def work_id(self, value):
        self._work_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiRetailWmsWorkQueryResponse, self).parse_response_content(response_content)
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'gmt_finished' in response:
            self.gmt_finished = response['gmt_finished']
        if 'notice_out_biz_no' in response:
            self.notice_out_biz_no = response['notice_out_biz_no']
        if 'notice_out_biz_type' in response:
            self.notice_out_biz_type = response['notice_out_biz_type']
        if 'operator' in response:
            self.operator = response['operator']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'remark' in response:
            self.remark = response['remark']
        if 'status' in response:
            self.status = response['status']
        if 'warehouse_code' in response:
            self.warehouse_code = response['warehouse_code']
        if 'work_details' in response:
            self.work_details = response['work_details']
        if 'work_id' in response:
            self.work_id = response['work_id']
