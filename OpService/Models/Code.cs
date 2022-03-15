using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using System.ComponentModel.DataAnnotations;

namespace OpService.Models
{
    public class Code
    {
        [Key]
        public string c_id {get;set;}
        public long c_status {get;set;}
        public string c_compile {get;set;}
        public string c_result {get;set;}
    }
}