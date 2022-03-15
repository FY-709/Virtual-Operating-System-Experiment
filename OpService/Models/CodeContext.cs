using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;

namespace OpService.Models
{
    public class CodeContext : DbContext 
    {
        public CodeContext(DbContextOptions<CodeContext> options) : base(options)
        {
        }
        public DbSet<Code> cdata { get; set; }
    }
}
